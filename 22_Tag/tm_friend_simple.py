import os
import re
import xlsxwriter
from datetime import datetime
import timeit

# tm 불러오기
from raw_tm_to_list import call_tagMT_ko_simple_lan
# tag 가져오기
from tag_finder import html_tag_creator
# 자주쓰이는 공통 함수
from common_function import excel_index_creator

# test용으로 simple의 한글 먼저 받아와서 돌리기
path_simple_list, ko_list = call_tagMT_ko_simple_lan('ko')


# 시작 한 개 씩
def find_directly_open(html_tag_kinds, sent):
    tag_found_start = list()
    tag_found_start_idx = list()
    for sdx in range(0, len(sent)):
        tag_start = ''
        html_tag_start_idx = 0
        html_tag_end_idx = 0
        html_tag_start_is = ''
        html_tag_start_idx_str = ''
        # 태그가 어떻게 생겼는지만 보기
        for html_tag in html_tag_kinds:
            tag_start_two = f'<{html_tag[0]}'
            if sent[sdx:sdx+len(tag_start_two)] != tag_start_two:
                continue
            elif sent[sdx:sdx+len(tag_start_two)] == tag_start_two:
                tag_start = f'<{html_tag}'
                len_html_tag = len(tag_start)
                # 태그의 길이 만큼 찾아보기
                for idx in range(sdx, len(sent)-len_html_tag):
                    # <span 같이 시작 찾기
                    if sent[idx:idx+len_html_tag] == tag_start:
                        html_tag_start_idx = idx
                        for jdx in range(html_tag_start_idx, len(sent)-len_html_tag):
                            # > 같이 끝 찾기
                            if sent[jdx] == '>':
                                html_tag_end_idx = jdx + 1
                                html_tag_start_is = sent[html_tag_start_idx:html_tag_end_idx]
                                html_tag_start_idx_str = f'{html_tag_start_idx}:{html_tag_end_idx}'
                                tag_found_start.append(html_tag_start_is)
                                tag_found_start_idx.append(html_tag_start_idx_str)
                                # print(html_tag_start_is)
                                break
                    break       
                break
    return tag_found_start, tag_found_start_idx


# 클로즈 한 개 씩        
def find_directly_close(html_tag_kinds, sent):
    tag_found_end = list()
    tag_found_end_idx = list()
    for sdx in range(0, len(sent)):
        tag_end = ''
        html_tag_start_idx = 0
        html_tag_end_idx = 0
        html_tag_end_is = ''
        html_tag_end_idx_str = ''
        # 태그가 어떻게 생겼는지만 보기
        for html_tag in html_tag_kinds:
            tag_end_two = f'</{html_tag[0]}'
            if sent[sdx:sdx+len(tag_end_two)] != tag_end_two:
                continue
            elif sent[sdx:sdx+len(tag_end_two)] == tag_end_two:
                tag_end = f'</{html_tag}'
                len_html_tag = len(tag_end)
                # 태그의 길이 만큼 찾아보기
                for idx in range(sdx, len(sent)-len_html_tag + 1):
                    # <span 같이 시작 찾기
                    if sent[idx:idx+len_html_tag] == tag_end:
                        # print(f'html_tag_start_idx: {idx}')
                        # print(sent[idx:idx+len_html_tag])
                        html_tag_start_idx = idx
                        for jdx in range(html_tag_start_idx, len(sent)):
                            # > 같이 끝 찾기
                            if sent[jdx] == '>':
                                # print(f'html_tag_end_idx: {jdx}')
                                # print(sent[html_tag_start_idx:html_tag_end_idx])
                                html_tag_end_idx = jdx + 1
                                html_tag_end_is = sent[html_tag_start_idx:html_tag_end_idx]
                                html_tag_end_idx_str = f'{html_tag_start_idx}:{html_tag_end_idx}'
                                tag_found_end.append(html_tag_end_is)
                                tag_found_end_idx.append(html_tag_end_idx_str)
                                break
                    break       
                break
    return tag_found_end, tag_found_end_idx


# 1개의 문장을 넣어주기 (str로 input)
def find_tag_idx(sent):
    
    # 태그 리스트 가져오기 (어떤 태그가 있는지 모르니깐 다 찾아주기)
    html_tag_kinds = html_tag_creator()
    # 태그 종류별로 탐색 (일단 1개만 찾아보기)
    
    html_tag_start, html_tag_start_idx = find_directly_open(html_tag_kinds, sent)
    html_tag_end, html_tag_end_idx = find_directly_close(html_tag_kinds, sent)

    return html_tag_start, html_tag_start_idx, html_tag_end, html_tag_end_idx
 
 
def test_excel(which_list):
    timestamp = datetime.now().strftime('%m%d%H%M')
    workbook = xlsxwriter.Workbook('./results/simple/simple_regex_test_ko' + timestamp + '_.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', 'path')
    worksheet.write('B1', 'Raw_TM')
    worksheet.write('C1', 'Tag_start')
    worksheet.write('D1', 'Tag_start_idx')
    worksheet.write('E1', 'Tag_end')
    worksheet.write('F1', 'Tag_end_idx')
    row_idx = 2 
    error_cnt = 0
    regular_cnt = 0

    for idx, sent in enumerate(which_list):

        tag_found, tag_found_idx, tag_found_close, tag_found_close_idx= find_tag_idx(sent)
        if len(tag_found) != len(tag_found_close):
            error_cnt += 1
            continue
        else:
            regular_cnt += 1
            a_idx = excel_index_creator('A', row_idx)
            b_idx = excel_index_creator('B', row_idx)

            worksheet.write(a_idx, path_simple_list[idx])
            worksheet.write(b_idx, sent)

            for idx in range(len(tag_found)):
                c_idx = excel_index_creator('C', row_idx)
                d_idx = excel_index_creator('D', row_idx)
                e_idx = excel_index_creator('E', row_idx)
                f_idx = excel_index_creator('F', row_idx)
                
                worksheet.write(c_idx, tag_found[idx])
                worksheet.write(d_idx, tag_found_idx[idx])
                worksheet.write(e_idx, tag_found_close[idx])
                worksheet.write(f_idx, tag_found_close_idx[idx])
                row_idx += 1
            
    workbook.close()
    print(f'error_cnt: {error_cnt}')
    print(f'regular_cnt: {regular_cnt}')

test_excel(ko_list)




                

               
                
        


