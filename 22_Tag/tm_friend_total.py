import os
import re
import xlsxwriter
from datetime import datetime
import timeit

# tm 불러오기
from create_raw_tm_to_list import call_tagMT_ko_total_lan

# 자주쓰이는 공통 함수
from common_function import excel_index_creator, html_tag_creator

# 추출하는 함수
from extractor import find_tag, stack_extractor

# test용으로 simple의 한글 먼저 받아와서 돌리기
lan = input(str())
path_total_list, lan_list = call_tagMT_ko_total_lan(lan)

 
 
def test_excel(which_list):
    start = timeit.default_timer()
    timestamp = datetime.now().strftime('%m%d%H%M')

    ########### error ###########
    workbook_error = xlsxwriter.Workbook('./results/total/error_total_regex_test_'+ lan + '_' + timestamp + '_.xlsx')
    worksheet_error = workbook_error.add_worksheet()
    worksheet_error.write('A1', 'path')
    worksheet_error.write('B1', 'Raw_TM')
    worksheet_error.write('C1', 'Tag_start')
    worksheet_error.write('D1', 'Tag_start_idx')
    worksheet_error.write('E1', 'Tag_end')
    worksheet_error.write('F1', 'Tag_end_idx')
    row_idx_error = 2

    ########### regular ###########
    workbook_regular = xlsxwriter.Workbook('./results/total/regular_total_regex_test_' + lan + '_' + timestamp + '_.xlsx')
    worksheet_regular = workbook_regular.add_worksheet()
    worksheet_regular.write('A1', 'path')
    worksheet_regular.write('B1', 'Raw_TM')
    worksheet_regular.write('C1', 'Tag_start')
    worksheet_regular.write('D1', 'Tag_start_idx')
    worksheet_regular.write('E1', 'Tag_end')
    worksheet_regular.write('F1', 'Tag_end_idx')
    row_idx = 2 

    error_cnt = 0
    regular_cnt = 0
    error_chunk = 0
    regular_chunk = 0

    for idx, sent in enumerate(which_list):
        print(f'{idx} - {sent}')
        tag_found, tag_found_idx, tag_found_close, tag_found_close_idx= stack_extractor(sent)
        # 길이가 안 맞을 때
        if len(tag_found) != len(tag_found_close):
            # tag_found_close가 더 작을 때
            if len(tag_found) - len(tag_found_close) > 0:
                distance = len(tag_found) - len(tag_found_close)
                for _ in range(distance):
                    tag_found_close.append('NA')
                    tag_found_close_idx.append('NA')

            # tag_found가 더 작을 때
            else:
                distance = len(tag_found_close) - len(tag_found)
                for _ in range(distance):
                    tag_found.append('NA')
                    tag_found_idx.append('NA')

            error_cnt += 1
            a_idx = excel_index_creator('A', row_idx_error)
            b_idx = excel_index_creator('B', row_idx_error)
            
            worksheet_error.write(a_idx, path_total_list[idx])
            worksheet_error.write(b_idx, sent)

            error_chunk += len(tag_found)

            for idx in range(len(tag_found)):
                c_idx = excel_index_creator('C', row_idx_error)
                d_idx = excel_index_creator('D', row_idx_error)
                e_idx = excel_index_creator('E', row_idx_error)
                f_idx = excel_index_creator('F', row_idx_error)
                
                worksheet_error.write(c_idx, tag_found[idx])
                worksheet_error.write(d_idx, tag_found_idx[idx])
                worksheet_error.write(e_idx, tag_found_close[idx])
                worksheet_error.write(f_idx, tag_found_close_idx[idx])
                row_idx_error += 1
        # 길이가 맞을 때
        else:
            regular_cnt += 1
            a_idx = excel_index_creator('A', row_idx)
            b_idx = excel_index_creator('B', row_idx)

            worksheet_regular.write(a_idx, path_total_list[idx])
            worksheet_regular.write(b_idx, sent)

            regular_chunk += len(tag_found)
            for idx in range(len(tag_found)):
                c_idx = excel_index_creator('C', row_idx)
                d_idx = excel_index_creator('D', row_idx)
                e_idx = excel_index_creator('E', row_idx)
                f_idx = excel_index_creator('F', row_idx)
                
                worksheet_regular.write(c_idx, tag_found[idx])
                worksheet_regular.write(d_idx, tag_found_idx[idx])
                worksheet_regular.write(e_idx, tag_found_close[idx])
                worksheet_regular.write(f_idx, tag_found_close_idx[idx])
                row_idx += 1

        print(f'{len(tag_found)} - {len(tag_found_close)}') 
        print('-'*50) 

    workbook_error.close()
    workbook_regular.close()
    stop = timeit.default_timer()
    print(f'take: {stop - start}')
    print(f'error_cnt: {error_cnt}')
    print(f'error_chunk: {error_chunk}\n')
    print(f'regular_cnt: {regular_cnt}')
    print(f'regular_chunk: {regular_chunk}')

test_excel(lan_list)




                

               
                
        






                

               
                
        


