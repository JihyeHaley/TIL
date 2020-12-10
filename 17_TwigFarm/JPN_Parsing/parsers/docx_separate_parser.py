"""
    docx_separate parser
"""

import timeit
import xlsxwriter
from itertools import zip_longest
from datetime import datetime
from nltk.tokenize import sent_tokenize

from utils.common_functions import *
from utils.regex_functions import *
from word_pos_extractor import *


stop_word = ['구분', '영문', '국문', '-', '번역', '번역본', '원문', '번역요청', '원본', 'NO', '제목', '타이틀', 'Title',
             '덕수궁관리소', '<참고>', '<영어>', '번역요청(영,일,중간,중번)', '영어:']


def docx_separate_to_excel(docx_ko_files, sub_path):
    if len(docx_ko_files) == 0:
        print('''-----------------------------------------------------------
        DOCX Seperate 파일 없습니다.
        ''')
    else:
        print('''-----------------------------------------------------------
        DOCX SEPERATE 작업 시작합니다.
        ''')
        timestamp = datetime.now().strftime("%m%d%H%M")

        print(" Total DOCX_KOR: ", len(docx_ko_files))


        # for timer
        start = timeit.default_timer()

        # ko , en로 분리된 파일 파싱 작업 시작.
        # 파일이름(경로포함)에서 "한.docx" 를 제외한 상태로 딕셔너리에 담겨있다.
        workbook = xlsxwriter.Workbook('./results/'  + sub_path  + '/' + sub_path  + '_docx_seperate_' + timestamp +'.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'PATH')
        worksheet.write('B1', 'Raw Data')
        worksheet.write('C1', 'KOR')
        worksheet.write('D1', 'ENG')
        
        row_idx = 2
        total_cnt = 0

        completed_log = open(f'./results/'  + sub_path  + '/' + sub_path + '_log_docx_' + timestamp + '.txt', "w+")
        docx_seperate_word_list_friend = list()
        for total_idx, each_file in enumerate(docx_ko_files):
            try:
                # Word to raw text
                # 한글 파일, 영문 파일 나뉘어있으므로 나누는 작업은 생략. 바로 정제를 시작한다.
                ko_contents = docx_to_raw_text(each_file, stop_word)

                kor_sent_list = []

                # raw paragraphs -> sentence tokenize
                for ko_lines in ko_contents:
                    kor_sents = sent_tokenize(ko_lines)  # nltk

                    for ko_sent in kor_sents:

                        # 토큰화된 문장에 한/영이 없으면 empty string = no insert
                        if neitherKoNorEn(ko_sent):
                            continue

                        kor_sent_list.append(ko_sent)

                 # 중복 제거
                kor_sent_list_full = list()
                for sent in kor_sent_list:
                    if sent not in kor_sent_list_full:
                        kor_sent_list_full.append(sent)
                # 총 몇줄인지 확인
                total_cnt += len(kor_sent_list_full)
                # print(f'{total_idx} - {len(kor_sent_list)}')

                for idx, krl in enumerate(kor_sent_list_full):
                    # 한글, 영어가 같이 있는게 아니라면 건너뛰기
                    if isSentKoreanAndEnglish(krl) == False:
                        continue

                    # A. Path 쓰기
                    a_idx =excel_index_creator('A', row_idx)
                    path = each_file.split('/')
                    path = f'{path[-3]}/{path[-2]}/{path[-1]}/{idx}'
                    worksheet.write(a_idx, path)

                    # raw _sent 형태소 분석 시작
                    # B. Raw Sent 쓰기
                    b_idx =excel_index_creator('B', row_idx)
                    worksheet.write(b_idx, krl)
                    ko_words, en_words = find_pattern_show_words(krl)
                    
                

                    for j in range(len(ko_words)):
                        # 중복 방지
                        if [ko_words[j], en_words[j]] in docx_seperate_word_list_friend:
                            continue
                        else:
                            docx_seperate_word_list_friend.append([ko_words[j], en_words[j]])
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
                                

                                row_idx += 1
                
                path = each_file.split('/')
                path = f'{path[-3]}/{path[-2]}/{path[-1]}'
                completed_log.write('[DONE READING]' + path + '\n')

            # Write Error log file when docx -> txt
            except Exception as e:
                print("DOCX_[ERROR]" + each_file + ":  " + str(e))
                completed_log.write('[ERROR MESSAGE]' + each_file + str(e) + '\n')
        
        workbook.close()
        completed_log.close()
        stop = timeit.default_timer()
       
        print(' DOCX_Seperate =====> Raw text to excel DONE (Running Time: ', stop - start, "sec.)")
        print(" Total Cnt:" + str(total_cnt) )