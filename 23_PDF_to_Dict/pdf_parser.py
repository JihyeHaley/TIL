'''
    pdf parser
'''

from datetime import datetime
import timeit
import xlsxwriter
from utils.common_functions import *
from utils.regex_functions import *
from utils.read_pdf import *
from tqdm import tqdm
import logging

skip_word = ['서론', '요약', '결론', '본론', '사사', '목차', '맺음말']

# Intro 제목
# title_regex = re.compile(r'((^\d\.|[Ⅰ|II|III|Ⅱ|Ⅲ|Ⅳ|Ⅴ|IV|V|VI]\.)(\d\.){0,}|^\d{1,}\))\s{0,}([\D[ㄱ-ㅣ가-힣|a-zA-Z].*)')
title_regex = re.compile(r'^(\d\.|[Ⅰ|II|III|Ⅱ|Ⅲ|Ⅳ|Ⅴ|IV|V|VI]\.)\s{0,}([\D[ㄱ-ㅣ가-힣|a-zA-Z].*)')

# 일반 웹사이트 주소
web_regex = re.compile(r'((http)s{0,1}://)?[\s]{0,1}[-a-z0-9]{0,3}\.{0,1}[-a-z0-9@:%._\\+~#=]{2,256}\.[a-z]{2,4}', re.IGNORECASE)

# 이메일주소
email_regex = re.compile(r'([a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}.{0,1}\w{0,4})', re.IGNORECASE)

# 전화번호 - 021231234(5), (02(2)-123(3)-1234), (02)988-9873, 1234-1234
phone_regex = re.compile(r'[\[<{\(]{0,1}(([\[<{\(]{0,1}[\☎\☏]{0,1}[\s]{0,1}[0-9]{0,3}[}>\)\]]{0,1}\-{0,1}[0-9]{3,4}\-{0,1}[0-9]{3,4})|([0-9]{9,10}))[}>\)\]]{0,1}')


def pdf_text_to_excel(pdf_file_list, sub_path):

    # for time stamp
    timestamp = datetime.now().strftime('%m%d%H%M')
    start = timeit.default_timer()

    # Open log files: record the order of file names
    # completed_log = open(f'./results/00_' + sub_path + '_PDF_LOG_' + timestamp + '.txt', "w+")
    logging.basicConfig(filename='./results/00_' + sub_path + '_PDF_LOG_' + timestamp + '.txt',
                        format='%(levelname)s:: %(message)s', level=logging.DEBUG)
    read_cnt = 0
    error_cnt = 0

    for each_file in tqdm(pdf_file_list):
        try:

            # log_file = os.path.join("./results/" + sub_path + each_file.split(sub_path)[-1] +".txt")

            # Open and create each excel file
            workbook = xlsxwriter.Workbook('./results/' + sub_path + each_file.split(sub_path, 1)[-1] + '.xlsx')
            worksheet = workbook.add_worksheet()
            worksheet.write('A1', 'FILE')
            worksheet.write('B1', 'KOR')
            row_idx = 2

            kor_raw_text = ""
            kor_sents = []
            read_cnt += 1

            # read pdf files and get as text list
            pdf_text_list = read_pdf_to_text(each_file)

            for line in pdf_text_list:
                each_line = line.strip()

                # 숫자만 남은 부분 - header 처리
                if each_line.isdigit():
                    continue

                if not each_line or only_char(each_line) or each_line.replace(' ', '') in skip_word \
                        or not isKorean(each_line):  # or len(each_line) < 6:
                    prev_cont = False
                    # continue

                elif check_fullmatch(web_regex, each_line) or check_fullmatch(email_regex, each_line) \
                        or check_fullmatch(phone_regex, each_line):
                    prev_cont = False
                    # continue

                else:

                    # list에만 추가
                    if check_fullmatch(title_regex, each_line):
                        prev_cont = False
                        kor_sents.append(each_line)
                        # continue

                    # *로 시작되는 인용문구 처리
                    elif bool(re.compile('^\*').match(each_line)):
                        prev_cont = False
                        kor_sents.append(each_line)

                    # 문장이 아니라 단어들의 나열의 경우 그냥 넣어준다
                    elif words_detect_pos(each_line):
                        kor_sents.append(each_line)
                        prev_cont = False
                        # continue

                    else:
                        # caption handle (stanza exception)
                        caption_regex = re.compile(r'((fig|figure|Fig|Figure|Table)\.)\s{0,}(\d)')
                        each_line = re.sub(caption_regex, r"\1\3", each_line)
                        kor_raw_text += each_line
                        prev_cont = True

                # 문단이 아닌 경우가 나왔을때 토큰화하여 문장 추가
                if kor_raw_text and not prev_cont:
                    kor_raw_text = re.sub(re.compile(r'(다\.)'), r'\1 ', kor_raw_text)
                    kor_raw_text = regex_cleaner_ko(kor_raw_text)
                    kor_raw_text = re.sub(re.compile(r'(\d.) (\d)'), r'\1\2', kor_raw_text)
                    kor_sents = [*kor_sents, *stanza_sentence_tokenizer(kor_raw_text, 'ko')]
                    kor_raw_text = ''

            # last paragraph tokenizing
            kor_raw_text = re.sub(re.compile(r'(다\.)'), r'\1 ', kor_raw_text)
            kor_raw_text = regex_cleaner_ko(kor_raw_text)
            kor_raw_text = re.sub(re.compile(r'(\d.) (\d)'), r'\1\2', kor_raw_text)
            kor_sents = [*kor_sents, *stanza_sentence_tokenizer(kor_raw_text, 'ko')]

            # writing excel file
            for ko_sent in kor_sents:

                # 토큰화 문장에 숫자/문자만 있으면 삭제
                if only_char(ko_sent):
                    continue

                # 토큰화 후 접속사 제거
                ko_sent = re.sub(r'((그러나|그리고|그러므로|하지만|따라서|그런데|또한|그래서)\,{0,1})', '', ko_sent).strip()

                # ' " 제거
                ko_sent = re.sub(r'[\'\"]', '', ko_sent).strip()

                #  문장시작이 ) } ] . : ; , - 인 경우 삭제
                ko_sent = re.sub(r'(^[↳\)\]\}\.\;\:\,\-\s]+)', '', ko_sent).strip()

                # 더블스페이스 싱글스페이스로 변경
                ko_sent = re.sub(r'(\s{2,})', ' ', ko_sent).strip()

                worksheet.write('A' + str(row_idx), '/' + sub_path + each_file.split(sub_path, 1)[-1])
                worksheet.write('B' + str(row_idx), ko_sent)
                row_idx += 1

            workbook.close()

            # with open(log_file, "w+") as my_log:
            #     for line in pdf_text_list:
            #         my_log.write(line+'\n')
            # print("Done !!")


            # Write Complete log
            # ompleted_log.write('[DONE READING]' + each_file + '\n')
            logging.info('[DONE READING] ' + each_file)
        # Write Error log file when docx -> txt
        except Exception as e:
            # completed_log.write('[ERROR]' + each_file + '.txt got ERROR! \n')
            # completed_log.write('[ERROR MESSAGE]' + str(e) + '\n')

            logging.error('[ERROR]' + each_file + '.txt got ERROR!')
            logging.error('[ERROR MESSAGE]' + str(e))
            print('[PDF ERROR]' + each_file + ' got ERROR!')
            print('[PDF ERROR MESSAGE]' + str(e) + '\n')
            error_cnt += 1

    #os.rename('./results/' + sub_path + '/00_FILE_log_' + timestamp + '.txt', './results/' + sub_path + '/00_'+ sub_path +'_log_' + timestamp + '.txt')
    # completed_log.write('\n' + 'Total PDF: ' + str(read_cnt))
    # completed_log.close()
    logging.info('Total PDF: ' + str(read_cnt))

    stop = timeit.default_timer()

    print(sub_path + ' Scanned files: ' + str(read_cnt-error_cnt) + ' (out of total ' + str(len(pdf_file_list)) + ' files)')
    print(sub_path + ' Total ERROR: ' + str(error_cnt) + '\n')
    print(sub_path + ' =====> Raw text to excel DONE (Running Time: ', stop - start, "sec.)")