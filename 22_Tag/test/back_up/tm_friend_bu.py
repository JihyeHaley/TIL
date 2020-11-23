import os
import re
import xlsxwriter
from datetime import datetime
import timeit


# test용으로 simple의 한글 먼저 받아와서 돌리기
test = ['<br><span_3><a_0>웹에서 보기</a><span_1> </span></h1><span_1> </span><a_2>인스타그램</a>']
test_2 =['<hr><img><hr></b><span_5>🦔</span></a><span_5>고슴이: 2주 만에 완전체 모습으로 만나니 더 반갑슴! </span>']
def html_tag_creator():
    # 꺽세 괄호 시작도 포함
    html_tag_delegates = ['p', 'span', 'a', 'b', 'strong', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'br', 'hr', 'img']
    return html_tag_delegates


#
# 시작 한 개 씩
def stack_extractor(sent):
    # 임시로 담을 리스트
    tag_found_open = list()
    tag_found_open_idx = list()
    tag_found_close = list()
    tag_found_close_idx = list()

    # 모든 sent에서 찾지 않고, <로 시작하는 것만 찾기
    remember_this_idx = list()

    # 결과물 담을 리스트
    tag_lists_open = list()
    tag_lists_open_idx = list()
    tag_lists_close = list()
    tag_lists_close_idx = list()

    html_tag_kinds = html_tag_creator()

    for sdx in range(0, len(sent), 1):
        if sent[sdx] == '<':
            remember_this_idx.append(sdx)

    for remember_this in remember_this_idx:
        tag_start = ''
        tag_start_idx = 0
        tag_end_idx = 0
        tag_is = ''
        tag_idx_str = ''
        # print(f'############################# 여기서부터 찾아: {remember_this}')
        # 태그가 어떻게 생겼는지만 보기
        for html_tag in html_tag_kinds:
            tag_start_two = f'<{html_tag[0]}'
            tag_end = f'</{html_tag}'
            # 시작 태그일때 
            if sent[remember_this:remember_this+len(tag_start_two)] == tag_start_two:
                tag_start = f'<{html_tag}'
                for idx in range(remember_this, len(sent)-len(tag_start)):
                    # <span 같이 시작 찾기
                    if sent[idx:idx+len(tag_start)] == tag_start:
                        tag_start_idx = idx
                        for jdx in range(tag_start_idx, len(sent)-len(tag_start)):
                            # > 같이 끝 찾기
                            if sent[jdx] == '>':
                                tag_end_idx = jdx + 1
                                tag_is = sent[tag_start_idx:tag_end_idx]
                                tag_idx_str = f'{tag_start_idx}:{tag_end_idx}'
                                if tag_is[:4] == '<img' or tag_is[:3] == '<br' or tag_is[:3] == '<hr':
                                    tag_found_close.append('Self_Close')
                                    tag_found_close_idx.append('Self_Close')
                                    tag_found_open.append(tag_is)
                                    tag_found_open_idx.append(tag_idx_str)  
                                else:
                                    tag_lists_open.append(tag_is)
                                    tag_lists_open_idx.append(tag_idx_str)
                                    
                                break
                    break
                
                                
            elif sent[remember_this:remember_this+len(tag_end)] == tag_end:
                for idx in range(remember_this, len(sent)-len(tag_end)):
                    tag_start_idx = idx
                    for jdx in range(tag_start_idx, len(sent)):
                        # > 같이 끝 찾기
                        if sent[jdx] == '>':
                            tag_end_idx = jdx + 1
                            tag_is = sent[tag_start_idx:tag_end_idx]
                            tag_idx_str = f'{tag_start_idx}:{tag_end_idx}'
                            tag_lists_close.append(tag_is)
                            tag_lists_close_idx.append(tag_idx_str)
                            break
                    
                    # 첫 시작이 끝 태그이면 tag_lists_open는 0 이라서
                    # <span_3> </h1> 이면 맞지 안으니깐 두번째 옵션에  ㅎㅎㅎ
                    if len(tag_lists_open) == 0 or tag_lists_open[-1][1:2] != tag_lists_close[-1][2:3]:
                        tag_found_close.append(tag_lists_close.pop())
                        tag_found_close_idx.append(tag_lists_close_idx.pop())
                        tag_found_open.append('tokenize_error')
                        tag_found_open_idx.append('tokenize_error') 
                    elif len(tag_lists_open) == 1:
                        tag_found_close.append('tokenize_error_no_close')
                        tag_found_close_idx.append('tokenize_error_no_close')
                        tag_found_open.append(tag_lists_open.pop())
                        tag_found_open_idx.append(tag_lists_open_idx.pop()) 
                    else:
                        tag_found_close.append(tag_lists_close.pop())
                        tag_found_close_idx.append(tag_lists_close_idx.pop())
                        tag_found_open.append(tag_lists_open.pop())
                        tag_found_open_idx.append(tag_lists_open_idx.pop())    
                    break
                            
    return tag_found_open, tag_found_open_idx, tag_found_close, tag_found_close_idx






def find_tag(sent):
    
    # 태그 종류별로 탐색 (일단 1개만 찾아보기)
    
    tag_found_start, tag_found_start_idx, tag_found_close, tag_found_close_idx = stack_extractor(sent)

    return tag_found_start, tag_found_start_idx, tag_found_close, tag_found_close_idx
 

def test_excel(which_list):

    error_cnt = 0
    regular_cnt = 0

    for idx, sent in enumerate(which_list):
        tag_found_start, tag_found_start_idx, tag_found_close, tag_found_close_idx = find_tag(sent)
        # tag_found_start, tag_found_start_idx, tag_found_close, tag_found_close_idx = chceck_find_list(tag_found_start, tag_found_start_idx, tag_found_close, tag_found_close_idx)
        print(f'sent: {sent}')
        print(f'tag_found: {tag_found_start}')
        print(f'tag_found_idx: {tag_found_start_idx}')
        print(f'tag_found_close: {tag_found_close}')
        print(f'tag_found_close_idx: {tag_found_close_idx}')
        print(f'{len(tag_found_start)}, {len(tag_found_close)}')
                
    # print(f'error_cnt: {error_cnt}')
    # print(f'regular_cnt: {regular_cnt}')

test_excel(test)