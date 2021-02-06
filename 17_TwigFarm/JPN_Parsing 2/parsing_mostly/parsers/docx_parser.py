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


def docx_parser_(docx_ko_files, sub_path):
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
        worksheet.write('A1', 'No')
        worksheet.write('B1', 'JPN')
        
        row_idx = 2
        total_cnt = 0


        docx_list = list()
        for total_idx, each_file in enumerate(docx_ko_files):
            try:
                # Word to raw text
                # 한글 파일, 영문 파일 나뉘어있으므로 나누는 작업은 생략. 바로 정제를 시작한다.
                raw_jap = docx_to_raw_text(each_file, stop_word)
                parsed = []

                # raw paragraphs -> sentence tokenize
                for sent__ in raw_jap:
                    parsed.append(sent__)
                # 총 몇줄인지 확인
                total_cnt += len(parsed)
                # print(f'{total_idx} - {len(kor_sent_list)}')

                for idx, sent in enumerate(parsed):
                    # A. Path 쓰기
                    a_idx =excel_index_creator('A', row_idx)
                    worksheet.write(a_idx, str(idx-1))
                    
                    # B. 일본어 쓰기
                    b_idx =excel_index_creator('B', row_idx)
                    worksheet.write(b_idx, sent)
                   

                    row_idx += 1

            # Write Error log file when docx -> txt
            except Exception as e:
                print("DOCX_[ERROR]" + each_file + ":  " + str(e))
                
        workbook.close()
        stop = timeit.default_timer()
       
        print(' DOCX_Seperate =====> Raw text to excel DONE (Running Time: ', stop - start, "sec.)")
        print(" Total Cnt:" + str(total_cnt) )