from datetime import datetime
import re
import xlsxwriter
import pandas as pd
import timeit

from utils.word_pos_utils import _start_mecab, _find_SL_idx, _extract_db_to_string, _check_mor_dict
from utils.common_functions import _excel_index_creator
from pdf_parser import _pdf_text_to_list


def word_extract_to_word(pdf_filtered_list, pdf_failed_list):
    
    timestamp = datetime.now().strftime('%m%d%H%M') # timestamp
    start = timeit.default_timer() # 작업 시작 시점

    ###################################
    # db 처리 엑셀 파일
    db_workbook = xlsxwriter.Workbook('./results/한국하천지명_pdf_추출문장_'  + timestamp +'.xlsx') 
    db_worksheet = db_workbook.add_worksheet()

    # 셀 색칠 
    cell_yellow = db_workbook.add_format()
    cell_yellow.set_pattern(1)
    cell_yellow.set_bg_color('yellow')

    # db 처리 엑셀 컬럼명
    db_worksheet.write('A1', 'No', cell_yellow)
    db_worksheet.write('B1', '원문', cell_yellow)
    db_worksheet.write('C1', '한글', cell_yellow)
    db_worksheet.write('D1', '한자', cell_yellow)
    db_worksheet.write('E1', '영어', cell_yellow)
    db_row_idx = 2


    ###################################
    # db 비처리 엑셀 파일
    failed_workbook = xlsxwriter.Workbook('./results/한국하천지명_pdf_비추출문장_'  + timestamp +'.xlsx') 
    failed_worksheet = failed_workbook.add_worksheet()

    # 셀 색칠 
    cell_red = failed_workbook.add_format()
    cell_red.set_pattern(1)
    cell_red.set_bg_color('red')

    # db 비처리 엑셀 컬럼명
    failed_worksheet.write('A1', 'No', cell_red)
    failed_worksheet.write('B1', '비처리 원문', cell_red)
    failed_worksheet.write('C1', 'm or km', cell_red)
    failed_row_idx = 2
    

    # analyze and write
    for filtered_sent in pdf_filtered_list:
        # 형태소 분석
        mor_list = _start_mecab(filtered_sent)
        
        # SL(영어 인덱 찾기)
        stop_idx = _find_SL_idx(mor_list)

        # mor[_][1] 패턴 추출 및 mor[_][0] 이어서 한글 한자 영어 패턴 확인 
        # kokoten = _check_mor_dict(mor_list, stop_idx)

        # mor_list에서 한글, 한자, 영어 추출해보기
        ko, kot, en = _extract_db_to_string(mor_list, stop_idx)

        # 모든 section이 다 채워져 있으면 작업하기
        if ko != '' and kot != '' and en != '':
            a_idx = _excel_index_creator('A', db_row_idx) 
            b_idx = _excel_index_creator('B', db_row_idx)
            c_idx = _excel_index_creator('C', db_row_idx)
            d_idx = _excel_index_creator('D', db_row_idx)
            e_idx = _excel_index_creator('E', db_row_idx)

            
            db_worksheet.write(a_idx, str(db_row_idx-1)) # a. no 
            db_worksheet.write(b_idx, filtered_sent) # b. 원문 
            db_worksheet.write(c_idx, ko) # c. 한글
            db_worksheet.write(d_idx, kot) # d. 한자
            db_worksheet.write(e_idx, en) # e. 영어

            db_row_idx += 1 # db_row_idx 더하기


        # 한 section이라도 비워져 있으면, pass -> 추출 안된 문장은 비추출 엑셀에 추가
        elif ko == '' or kot == '' or en =='':
            a_idx = _excel_index_creator('A', failed_row_idx)
            b_idx = _excel_index_creator('B', failed_row_idx)
            c_idx = _excel_index_creator('C', failed_row_idx)
            
            failed_worksheet.write(a_idx, str(failed_row_idx-1)) # No
            failed_worksheet.write(b_idx, filtered_sent) # 비처리 원문
            failed_worksheet.write(c_idx, 'k or km') # m or km 유무

            failed_row_idx += 1 # failed_row_idx 더하기
            continue
    db_workbook.close()

    # 추출하지 않은 모든 파일 다시 적기
    for failed_sent in pdf_failed_list:
        a_idx = _excel_index_creator('A', failed_row_idx)
        b_idx = _excel_index_creator('B', failed_row_idx)
        c_idx = _excel_index_creator('C', failed_row_idx)
        
        failed_worksheet.write(a_idx, str(failed_row_idx-1)) # No
        failed_worksheet.write(b_idx, failed_sent) # 비처리 원문
        failed_worksheet.write(c_idx, '') # m or km 유무

        failed_row_idx += 1 # failed_row_idx 더하기

    failed_workbook.close()
    stop = timeit.default_timer() # 작업 시작 시점

    print(f'word_extract_to_word Running Time: {stop - start} sec')
