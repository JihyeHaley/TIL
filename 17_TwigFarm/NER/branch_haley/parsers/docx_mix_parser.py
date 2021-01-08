'''
    docx_mix_parser (병합)
    Word -> HTML raw text -> Excel 으로 변환
    문장 단위 1차 정제 후 엑셀 파일 생성
'''

import mammoth
import timeit
import xlsxwriter
from itertools import zip_longest
from datetime import datetime
from nltk.tokenize import sent_tokenize

from utils.common_functions import *
from utils.regex_functions import *


stop_word = ['구분', '영문', '국문', '-', '번역', '번역본', '원문', '번역요청', '원본', 'NO', '제목', '타이틀', 'Title',
             '덕수궁관리소', '<참고>', '<영어>', '번역요청(영,일,중간,중번)', '영어:']

# 파일을 돌리는 해당 경로에 결과 엑셀 생성
def docx_mix_to_excel(root_dir, sub_dir):

    timestamp = datetime.now().strftime('%m%d%H%M')
    file_path = root_dir + sub_dir

    # path별 문서 list를 가져옴
    docx_name_lists = get_filename_list(file_path, '.docx')
    print(sub_dir + ' Total docx: ', len(docx_name_lists))

    # Open and create excel file
    workbook = xlsxwriter.Workbook(sub_dir + "_excel_" + timestamp + '.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write('B1', 'KOR')
    worksheet.write('C1', 'ENG')
    row_idx = 2

    # Open log files: record the order of file names
    completed_log = open(f'./log_' + sub_dir + '_' + timestamp + '.txt', "w+")
    read_cnt = 0
    error_cnt = 0

    # for timer
    start = timeit.default_timer()

    for each_file in docx_name_lists:

        filename = each_file.split('/')[-1]

        # 한/영 병합 문서 파일만 파싱작업
        if filename[-6] == '병': #and filename != '관광-2018한국관광공사-101.마포서교동주민센터__골목여행지도-병.docx':
            read_cnt += 1
            try:
                # 문서간 구분을 위해 추가
                worksheet.write('A' + str(row_idx), ">" * 10)
                worksheet.write('B' + str(row_idx), ">" * 10 + filename)
                row_idx += 1

                # Word to raw text
                contents = docx_to_raw_text(each_file, stop_word)

                ## 각 문서종류별 폴더 안에 파싱된 txt 파일 추가, 폴더가 없으면 생성
                # pathlib.Path('./' + sub_dir + '_txt').mkdir(parents=True, exist_ok=True)
                # txt_path = os.path.join(f'./' + sub_dir + '_txt/', filename + ".txt")
                # all_words = open(txt_path, "w+")

                kor_raw_list = []
                eng_raw_list = []

                kor_sent_list = []
                eng_sent_list = []

                for lines in contents:

                    each_line = lines.strip()

                    # Kor or Kor/Eng
                    if not mustEnglish(each_line) and isKorean(each_line):

                        # Kor and Enl - split (영어 두단어 이상 기준)
                        if isEnglish(each_line):
                            kor_and_eng = split_kor_eng(each_line)
                            for both_lang in kor_and_eng:
                                if both_lang.strip() and mustEnglish(both_lang):
                                    eng_raw_list.append(both_lang)
                                elif both_lang.strip() and not mustEnglish(both_lang):
                                    kor_raw_list.append(both_lang)

                        else:
                            # 한글 or 영어없는 공백,숫자,특수문자
                            kor_raw_list.append(each_line)

                    # 영어
                    elif mustEnglish(each_line) and not isKorean(each_line):
                        eng_raw_list.append(each_line)

                # Remove empty string
                kor_raw_list = list(filter(None, kor_raw_list))
                eng_raw_list = list(filter(None, eng_raw_list))

                
                # raw paragraphs -> sentence tokenize
                for ko_lines in kor_raw_list:
                    kor_sents = sent_tokenize(strip_regex_all(ko_lines))  # nltk

                    for ko_sent in kor_sents:
                        
                        # 토큰화된 문장에 한/영이 없으면 empty string = no insert
                        if neitherKoNorEn(ko_sent):
                            continue

                        kor_sent_list.append(ko_sent)

                for en_lines in eng_raw_list:
                    eng_sents = sent_tokenize(strip_regex_all(en_lines))  # nltk

                    for en_sent in eng_sents:
                        
                        # 토큰화된 문장에 한/영이 없으면 empty string = no insert
                        if neitherKoNorEn(en_sent):
                            continue

                        eng_sent_list.append(en_sent)
                # ----------------------------------------

                # Write Excel file
                for ko, en in zip_longest(kor_sent_list, eng_sent_list, fillvalue=' '):
                    worksheet.write('B' + str(row_idx), str(ko))
                    worksheet.write('C' + str(row_idx), str(en))
                    row_idx += 1

                # Write Complete log
                completed_log.write('[DONE READING]' + filename + ' \n\n')

            # Write Error log file when docx -> txt
            except Exception as e:
                completed_log.write('[ERROR]' + filename + '.txt got ERROR! \n')
                completed_log.write('[ERROR MESSAGE]' + str(e) + '\n')
                print('[ERROR]' + filename + ' got ERROR! \n')
                error_cnt += 1
        
        else:
            print('\tSKIP FILE: ', filename)
            completed_log.write('[!!!SKIP FILE]' + filename + '\n')
            
    completed_log.close()
    workbook.close()

    stop = timeit.default_timer()

    print(sub_dir + ' ----> Raw text to excel DONE (Running Time: ', stop - start, "sec.)")
    print(sub_dir + ' 한/영 병합 파일 수: ' + str(read_cnt) + ' (out of total ' + len(docx_name_lists) +' files)')
    print(sub_dir + ' Total ERROR: ', error_cnt)
