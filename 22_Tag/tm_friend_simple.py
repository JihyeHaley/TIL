import os
import re
import xlsxwriter
from datetime import datetime
import timeit

# tm 불러오기 (lan선택)
# from tm_to_list import call_tagMT_simple_lan
# tm 불러오기 (lan 전체)
from tm_to_list import call_tagMT_simple

# 자주쓰이는 공통 함수
from common_function import excel_index_creator, html_tag_creator

# 추출하는 함수
from tag_extractor import stack_extractor, plain_text_extractor


path_simple_list, ko_simple_list, en_simple_list, ja_simple_list = call_tagMT_simple()

lan_simple_dict = dict()
lan_simple_dict['ko'] = ko_simple_list
lan_simple_dict['en'] = en_simple_list
lan_simple_dict['ja'] = ja_simple_list


def tm_simple_extract_excel(lan_simple_list):
    start = timeit.default_timer()
    timestamp = datetime.now().strftime('%m%d%H%M')
    ########### error ###########
    '''print만 보기'''

    ########### regular ###########
    workbook_normal = xlsxwriter.Workbook('./results/simple/normal_simple_' +  timestamp + '_.xlsx')
    worksheet_normal_ko = workbook_normal.add_worksheet()
    worksheet_normal_en = workbook_normal.add_worksheet()
    worksheet_normal_ja = workbook_normal.add_worksheet()

    worksheet_normal_ko.write('A1', 'path')
    worksheet_normal_ko.write('B1', 'ko')
    worksheet_normal_ko.write('C1', 'Tag_start')
    worksheet_normal_ko.write('D1', 'Plain_text')

    worksheet_normal_en.write('A1', 'path')
    worksheet_normal_en.write('B1', 'en')
    worksheet_normal_en.write('C1', 'Tag_start')
    worksheet_normal_en.write('D1', 'Plain_text')

    worksheet_normal_ja.write('A1', 'path')
    worksheet_normal_ja.write('B1', 'ja')
    worksheet_normal_ja.write('C1', 'Tag_start')
    worksheet_normal_ja.write('D1', 'Plain_text')

    for key, value in lan_simple_dict.items():
        row_idx = 2 
        error_cnt = 0
        normal_cnt = 0
        error_chunk = 0
        normal_chunk = 0

        # ko
        if key == 'ko':
            for idx, sent in enumerate(value):
                tag_found_start, tag_found_start_idx, tag_found_close, tag_found_close_idx= stack_extractor(sent)
                plain_text_list, tag_found_start_output = plain_text_extractor(sent, tag_found_start, tag_found_start_idx, tag_found_close_idx)

                # 길이가 안 맞을 때
                if len(plain_text_list) != len(tag_found_start_output):
                    error_cnt += 1
                
                else:
                    normal_cnt += 1
                    a_idx = excel_index_creator('A', row_idx)
                    b_idx = excel_index_creator('B', row_idx)

                    worksheet_normal_ko.write(a_idx, path_simple_list[idx])
                    worksheet_normal_ko.write(b_idx, sent)

                    normal_chunk += len(plain_text_list)
                    for idx in range(len(plain_text_list)):
                        c_idx = excel_index_creator('C', row_idx)
                        d_idx = excel_index_creator('D', row_idx)
                    
                        
                        worksheet_normal_ko.write(c_idx, tag_found_start_output[idx])
                        worksheet_normal_ko.write(d_idx, plain_text_list[idx])
                        row_idx += 1

        elif key == 'en':
            for idx, sent in enumerate(value):
                tag_found_start, tag_found_start_idx, tag_found_close, tag_found_close_idx= stack_extractor(sent)
                plain_text_list, tag_found_start_output = plain_text_extractor(sent, tag_found_start, tag_found_start_idx, tag_found_close_idx)

                # 길이가 안 맞을 때
                if len(plain_text_list) != len(tag_found_start_output):
                    error_cnt += 1
                
                else:
                    normal_cnt += 1
                    a_idx = excel_index_creator('A', row_idx)
                    b_idx = excel_index_creator('B', row_idx)

                    worksheet_normal_en.write(a_idx, path_simple_list[idx])
                    worksheet_normal_en.write(b_idx, sent)

                    normal_chunk += len(plain_text_list)
                    for idx in range(len(plain_text_list)):
                        c_idx = excel_index_creator('C', row_idx)
                        d_idx = excel_index_creator('D', row_idx)
                    
                        
                        worksheet_normal_en.write(c_idx, tag_found_start_output[idx])
                        worksheet_normal_en.write(d_idx, plain_text_list[idx])
                        row_idx += 1

        elif key == 'ja':
            for idx, sent in enumerate(value):
                tag_found_start, tag_found_start_idx, tag_found_close, tag_found_close_idx= stack_extractor(sent)
                plain_text_list, tag_found_start_output = plain_text_extractor(sent, tag_found_start, tag_found_start_idx, tag_found_close_idx)

                # 길이가 안 맞을 때
                if len(plain_text_list) != len(tag_found_start_output):
                    error_cnt += 1
                
                else:
                    normal_cnt += 1
                    a_idx = excel_index_creator('A', row_idx)
                    b_idx = excel_index_creator('B', row_idx)

                    worksheet_normal_ja.write(a_idx, path_simple_list[idx])
                    worksheet_normal_ja.write(b_idx, sent)

                    normal_chunk += len(plain_text_list)
                    for idx in range(len(plain_text_list)):
                        c_idx = excel_index_creator('C', row_idx)
                        d_idx = excel_index_creator('D', row_idx)
                    
                        
                        worksheet_normal_ja.write(c_idx, tag_found_start_output[idx])
                        worksheet_normal_ja.write(d_idx, plain_text_list[idx])
                        row_idx += 1
        
        print(f'key: {key}')
        print(f'error_cnt: {error_cnt}')
        print(f'error_chunk: {error_chunk}')
        print(f'normal_cnt: {normal_cnt}')
        print(f'normal_chunk: {normal_chunk}')
        print('-'*50)
    
        
    workbook_normal.close()
    stop = timeit.default_timer()
    print(f'take: {stop - start}')
    

tm_simple_extract_excel(lan_simple_dict)