'''
    docx_single_parser
'''

import timeit
import xlsxwriter
from datetime import datetime
from nltk.tokenize import sent_tokenize
import kss

from utils.common_functions import *
from utils.regex_functions import *

stop_word = ['서론', '요약', '결론']  # Fig., 사사?


# Find all files in the path and subdirectories (having parameter ext)
def get_filename_list(path, ext):
    # ver2: Encoding 문제로 convmv로 convert 후 read
    files_dict = {}
    print('Read files and change encoding.......\\')

    for f in Path(path).rglob(f'*{ext}'):
        if str(f.parent) not in files_dict.keys():
            files_dict[str(f.parent)] = [f.name]
        else:
            files_dict[str(f.parent)].append(f.name)

    return files_dict



# 제 1호, 제 4권
def section_regex(text):
    section_regex = re.compile(r'제[\s]{0,1}(\d){0,1}[호|권]')
    return bool(section_regex.fullmatch(text))


# normalized file names
def nfd2nfc(data):
    return normalize('NFC', data)



# Intro 제목 지우기
intro_regex = re.compile(r'[Ⅰ|Ⅱ|Ⅲ|Ⅳ|Ⅴ|Ⅵ|Ⅶ]\s{0,1}\.{0,1}')

# 일반 웹사이트 주소 지우기
web_regex = re.compile(r'((http)s{0,1}://)?[\s]{0,1}[-a-z0-9]{0,3}\.{0,1}[-a-z0-9@:%._\\+~#=]{2,256}\.[a-z]{2,4}',
                       re.IGNORECASE)

# 이메일주소 지우기
email_regex = re.compile(r'([a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}.{0,1}\w{0,4})', re.IGNORECASE)

# 전화번호 지우기 - 021231234(5), (02(2)-123(3)-1234), (02)988-9873, 1234-1234
phone_regex = re.compile(
    r'[\[<{\(]{0,1}(([\[<{\(]{0,1}[\☎\☏]{0,1}[\s]{0,1}[0-9]{0,3}[}>\)\]]{0,1}\-{0,1}[0-9]{3,4}\-{0,1}[0-9]{3,4})|([0-9]{9,10}))[}>\)\]]{0,1}')

# 날짜 지우기 - yyyy.mm.dd | mm.dd.yyyy | dd.mm.yyyy
date_regex = re.compile(
    r'((\d{4})([\s./-]{0,3})(0[1-9]|1[012]|[1-9])([\s./-]{0,3})(0[1-9]|[12][0-9]|3[0-1]|[1-9])([\s./-]{0,3}))' \
    '|((0[1-9]|1[012]|[1-9])([\s./-]{0,3})(0[1-9]|[12][0-9]|3[0-1]|[1-9])([\s./-]{0,3})(\d{4})([\s./-]{0,3}))' \
    '|((0[1-9]|[12][0-9]|3[0-1]|[1-9])([\s./-]{0,3})(0[1-9]|1[012]|[1-9])([\s./-]{0,3})(\d{4})([\s./-]{0,3}))')

# [숫자 + . + 공백 + 단어] -> [숫자 + . + 단어]: 공백제거
numbering_regex = re.compile(r'(\d)\.\s(\w)')

# 문장중간에 . 들어있는지 확인
mid_dot_regex = re.compile(r'(?!\d\.\d)\w{2,}\.[\w([*.,]')  # r'\w\..'

# fig. 1 -> kss
kss_regex = re.compile(r'(?!\d\.\d)\w\.\s\d')


# 파일을 돌리는 해당 경로에 결과 엑셀 생성
def raw_single_docx_to_excel(root_dir):
    # for time stamp
    timestamp = datetime.now().strftime('%m%d%H%M')

    # for timer
    start = timeit.default_timer()

    # path별 문서 list를 가져옴
    docx_name_dict = get_filename_list(root_dir, '.docx')
    total_file_cnt = sum(map(len, docx_name_dict.values()))
    print('Total docx: ', total_file_cnt)

    root_name = root_dir.split('/')[-1]

    # Open and create excel file
    workbook = xlsxwriter.Workbook('./results/' + root_name + '_all_excel_v2_' + timestamp + '.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write('B1', 'KOR')
    row_idx = 2

    # Open log files: record the order of file names
    #     pathlib.Path('./results/' + sub_dir).mkdir(parents=True, exist_ok=True)
    completed_log = open(f'./results/' + root_name + '_log_v2_' + timestamp + '.txt', "w+")
    read_cnt = 0
    error_cnt = 0

    print('Writing all files ......')
    for dir_key, file_list in docx_name_dict.items():

        # convert unicode normalization
        normalized_dir = nfd2nfc(dir_key)

        sub = "/".join(normalized_dir.split('/')[-2:])

        for filename in file_list:
            read_cnt += 1
            try:
                # 문서간 구분을 위해 추가
                worksheet.write('A' + str(row_idx), ">" * 10)
                worksheet.write('B' + str(row_idx), "> " * 10 + "/" + sub + "/" + filename)
                row_idx += 1

                # Word to raw text
                raw_texts = docx_to_raw_text(dir_key + "/" + filename, stop_word)

                kor_raw_list = []
                kor_sent_list = []

                for lines in raw_texts:
                    each_line = lines.strip()
                    kor_raw_list.append(each_line)

                # raw paragraphs -> sentence tokenize
                for ko_lines in kor_raw_list:

                    ko_lines = remove_regex(r'\=', ko_lines)
                    ko_lines = remove_regex(intro_regex, ko_lines)
                    ko_lines = remove_regex(web_regex, ko_lines)
                    ko_lines = remove_regex(email_regex, ko_lines)
                    ko_lines = remove_regex(phone_regex, ko_lines)

                    if re.search(kss_regex, ko_lines.strip()):
                        # kss
                        kor_sents = kss.split_sentences(ko_lines)

                    elif re.match(numbering_regex, ko_lines.strip()):
                        # kss
                        kor_sents = kss.split_sentences(ko_lines)

                    elif re.search(mid_dot_regex, ko_lines.strip()):
                        # kss
                        kor_sents = kss.split_sentences(ko_lines)

                    elif mustEnglish(ko_lines.strip()):
                        # stanza
                        kor_sents = sentence_tokenizer(ko_lines, 'en')
                    else:
                        # nltk
                        kor_sents = sent_tokenize(ko_lines)
                    # kor_sents = sentence_tokenizer(ko_lines, 'ko')  #stanza

                    for ko_sent in kor_sents:
                        kor_sent_list.append(ko_sent)

                # ----------------------------------------

                # Write Excel file
                for ko in kor_sent_list:
                    worksheet.write('B' + str(row_idx), str(ko))
                    row_idx += 1

                # Write Complete log
                completed_log.write('[DONE READING]' + sub + "_" + filename + ' \n\n')

            # Write Error log file when docx -> txt
            except Exception as e:
                completed_log.write('[ERROR]' + sub + "_" + filename + '.txt got ERROR! \n')
                completed_log.write('[ERROR MESSAGE]' + str(e) + '\n')
                print('[ERROR]' + sub + "_" + filename + ' got ERROR! \n')
                error_cnt += 1

    print(root_name + ' Scanned files: ' + str(read_cnt) + ' (out of total ' + str(len(file_list)) + ' files)')
    print(root_name + ' Total ERROR: ' + str(error_cnt) + '\n')

    completed_log.close()
    workbook.close()

    stop = timeit.default_timer()
    print(root_name + ' =====> Raw text to excel DONE (Running Time: ', stop - start, "sec.)")
