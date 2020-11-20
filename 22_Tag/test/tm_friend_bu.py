import os
import re
import xlsxwriter
from datetime import datetime
import timeit


# test용으로 simple의 한글 먼저 받아와서 돌리기
test = ['<span_3><a_0>웹에서 보기</a><span_1> </span><span_1> </span><a_2>인스타그램</a></span>', '<span_5>🦔</span><span_5>고슴이: 2주 만에 완전체 모습으로 만나니 더 반갑슴! </span>']
def html_tag_creator():
    # 꺽세 괄호 시작도 포함
    html_tag_delegates = ['p', 'span', 'a', 'b', 'strong', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'br', 'hr', 'img']
    return html_tag_delegates


# 시작 한 개 씩
def stack_extractor(html_tag_kinds, sent):
    tag_found_start = list()
    tag_found_start_idx = list()
    tag_found_close = list()
    tag_found_close_idx = list()
    remember_this_idx = list()
    tag_lists_open = list()
    tag_lists_open_idx = list()
    tag_lists_close = list()
    tag_lists_close_idx = list()
    for sdx in range(0, len(sent), 1):
        if sent[sdx] == '<':
            remember_this_idx.append(sdx)
    
    for remember_this in remember_this_idx:
        print(sent)
        tag_start = ''
        tag_start_idx = 0
        tag_end_idx = 0
        tag_is = ''
        tag_idx_str = ''
        print(f'여기서부터 찾아: {remember_this}')
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
                                print(tag_is)
                                tag_lists_open.append(tag_is)
                                tag_lists_open_idx.append(tag_idx_str)
                                print(tag_lists_open)
                                print('-'*40)
                                break
                    break
            
                                

            elif sent[remember_this:remember_this+len(tag_end)] == tag_end:
                for idx in range(remember_this, len(sent)-len(tag_end)):
                    tag_start_idx = idx
                    for jdx in range(tag_start_idx, len(sent)-len(tag_end)):
                        # > 같이 끝 찾기
                        if sent[jdx] == '>':
                            tag_end_idx = jdx + 1
                            tag_is = sent[tag_start_idx:tag_end_idx]
                            print(tag_is)
                            tag_idx_str = f'{tag_start_idx}:{tag_end_idx}'
                            tag_lists_close.append(tag_is)
                            tag_lists_close_idx.append(tag_idx_str)
                            break
                            
                    # pop 처리할 아이 전처리하기
                    print(tag_lists_open[-1], tag_lists_close[-1])
                    tag_found_close.append(tag_lists_close.pop())
                    tag_found_close_idx.append(tag_lists_close_idx.pop())
                    tag_found_start.append(tag_lists_open.pop())
                    tag_found_start_idx.append(tag_lists_open_idx.pop())    
                    print('#'*30)
                    print(f'tag_lists_close: {tag_lists_close}\n')        
                    print(f'tag_lists_open: {tag_lists_open}\n')   
                    print('-'*40)     
                    break
                                
    
    return tag_found_start, tag_found_start_idx, tag_found_close, tag_found_close_idx


def find_tag(sent):
    
    # 태그 리스트 가져오기 (어떤 태그가 있는지 모르니깐 다 찾아주기)
    html_tag_kinds = html_tag_creator()
    # 태그 종류별로 탐색 (일단 1개만 찾아보기)
    
    tag_found_start, tag_found_start_idx, tag_found_close, tag_found_close_idx = stack_extractor(html_tag_kinds, sent)

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
                
    # print(f'error_cnt: {error_cnt}')
    # print(f'regular_cnt: {regular_cnt}')

test_excel(test)