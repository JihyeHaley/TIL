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
from mecab import *

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
def raw_single_docx_to_excel(docx_ko_files, sub_path):
    
    # for time stamp
    timestamp = datetime.now().strftime('%m%d%H%M')

    # for timer
    start = timeit.default_timer()

    if len(docx_ko_files) == 0:
        print('''-----------------------------------------------------------
        DOCX Single 파일 없습니다.
        ''') 
    else:
        print('Total docx: ', str(len(docx_ko_files)))

        # ----------------------------------------
        workbook = xlsxwriter.Workbook('./results/'   + sub_path  + '/' + sub_path  + '/' + sub_path + '_docx_single_' + timestamp +'.xlsx') # _mustbessossc
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'PATH')
        worksheet.write('B1', 'Raw Data')
        worksheet.write('C1', 'KOR')
        worksheet.write('D1', 'ENG')
        # worksheet.write('E1', 'MOR')
        # worksheet.write('F1', '매캡')
        row_idx = 2
        total_cnt = 0

        completed_log = open(f'./results/'  + sub_path  + '/' + sub_path + '_log_docx_single_' + timestamp + '.txt', "w+")

        print('Writing all files ......')
        
        print('''-----------------------------------------------------------
        DOCX SINGLE 작업 시작합니다.
        ''')
        print(" Total PPTX_FILES: ", len(docx_ko_files))
        # Open and create each excel file
        workbook = xlsxwriter.Workbook('./results/' + sub_path  + '/'  + sub_path  + '_xlsx_' + timestamp +'.xlsx') # _mustbessossc
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'PATH')
        worksheet.write('B1', 'Raw Data')
        worksheet.write('C1', 'KOR')
        worksheet.write('D1', 'ENG')
        # worksheet.write('E1', 'MOR')
        # worksheet.write('F1', '매캡')
        row_idx = 2
        total_cnt = 0
        # eng_kor = 0
        completed_log = open(f'./results/'  + sub_path  + '/' + sub_path + '_log_xlsx_' + timestamp + '.txt', "w+")
        
        for total_idx, filename in enumerate(docx_ko_files):
            try:
                # Word to raw text
                raw_texts = docx_to_raw_text(dir_key + "/" + filename, stop_word)

                kor_raw_list = []
                kor_sent_list = []

                for lines in raw_texts:
                    each_line = lines.strip()
                    kor_raw_list.append(each_line)

                # raw paragraphs -> sentence tokenize
                for ko_lines in kor_raw_list:

                    # ko_lines = remove_regex(r'\=', ko_lines)
                    # ko_lines = remove_regex(intro_regex, ko_lines)
                    # ko_lines = remove_regex(web_regex, ko_lines)
                    # ko_lines = remove_regex(email_regex, ko_lines)
                    # ko_lines = remove_regex(phone_regex, ko_lines)

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


                # 중복 제거
                kor_sent_list = list(set(kor_sent_list))
                # 총 몇줄인지 확인
                total_cnt += len(kor_sent_list)
                # print(f'{total_idx} - {len(kor_sent_list)}')

                for ko_list in kor_sent_list:
                    for idx, raw_sent in enumerate(ko_list):
                        # 한글, 영어가 같이 있는게 아니라면 건너뛰기
                        if isSentKoreanAndEnglish(raw_sent) == False:
                            continue
                        
                        # A. Path 쓰기
                        a_idx =excel_index_creator('A', row_idx)
                        path = f'{root_name}/{filename}/{idx}' 
                        worksheet.write(a_idx, path)

                        # raw _sent 형태소 분석 시작
                        # B. Raw Sent 쓰기
                        b_idx =excel_index_creator('B', row_idx)
                        worksheet.write(b_idx, raw_sent)
                        te, ko_words, en_words, mor_match_list_str = find_pattern_show_words(raw_sent)
                        # print('word_matched: ', word_matched)

                        # F. 형태소 분석되는 세세한 것들 쓰기
                        # f_idx =excel_index_creator('F', row_idx)
                        # worksheet.write(f_idx, te)
                        # print(te)
                        

                        for j in range(len(ko_words)):

                            # D의 개수가 1개면 skip
                            en_words[j] = en_words[j].strip(' ')
                            if skip_mored_word(en_words[j]) == True:
                                continue

                            else:
                                # C.  ko_word 쓰기
                                c_idx =excel_index_creator('C', row_idx)
                                worksheet.write(c_idx, ko_words[j])


                                # D.  en_word 쓰기
                                d_idx = excel_index_creator('D', row_idx)
                                worksheet.write(d_idx, en_words[j])
                                

                                # E.  형태소 패턴 쓰기 (확인을 원할때 사용 print or excel에 작성)
                                # Excel 작성
                                # e_idx = excel_index_creator('E', row_idx)
                                
                                # length가 다를때는 일단 넘어가고 
                                # 형태소 어떤 패턴으로 뽑앗는지 확인하기
                                # print해서 확인
                                # if len(ko_words) != len(mor_match_list_str):
                                    # continue
                                # length가 같을때는 쓰게 만들기
                                # worksheet.write(e_idx, mor_match_list_str[j])
                                # print(mor_match_list_str[j])
                                
                                # 다음에 쓰여질 줄을 위해서 row_idx += 1
                                row_idx += 1

                completed_log.write('[DONE READING]' + filename + '\n')
            # Write Error log file when docx -> txt
            except Exception as e:  
                print('[ERROR]' + sub_path + "_" + filename + ' got ERROR! \n')
                completed_log.write('[ERROR MESSAGE]' + filename + str(e) + '\n')

        workbook.close()
        completed_log.close()
        stop = timeit.default_timer()

    print(' =====> Raw text to excel DONE (Running Time: ', stop - start, "sec.)")
