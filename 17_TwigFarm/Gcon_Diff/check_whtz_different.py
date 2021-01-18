import re
import timeit

from konlpy.tag import Mecab
from datetime import datetime


# 형태소 분석
def in_start_mecab(sent):
    m = Mecab()
    mor_list = m.pos(sent)
    ''' te -> list > tuple > str'''
    return mor_list


# 마지막 인덱스인지 체크
def in_whether_last_idx(idx, words_list):
    length = len(words_list)
    if idx == length - 1:
        return True
    elif idx != length - 1:
        return False


# 앞 글자만 가져오기
def _leave_only_words(sent):
    mor_list = in_start_mecab(sent)
    words_list = list()
    for mor_tuple in mor_list:
        words_list.append(mor_tuple[0])
    return words_list


# find what is different components in the sentence
def _find_start_stop_idx(a_mor, b_mor, c_mor):
    diff_idx = 0 # 인덱스 
    diff_list = list() # 인덱스 리스트 초기화
    for idx in range(len(a_mor)):
        if a_mor[idx] == b_mor[idx] == c_mor[idx]:
            continue
        else: 
            diff_idx = idx
        diff_list.append(diff_idx)
           
    return diff_list


# <b> 넣어주면서 글쓰기 change diff words
def _change_diff_words(a_mor, b_mor, c_mor, diff_list):
    a_completed, b_completed, c_completed = '', '', '' 
    pre_output_result_list = list() # 초기화

    for idx in range(len(a_mor)):
        # 다릏다고 판단된 아이는 <b></b>
        if idx in diff_list:
            a_mor[idx] += f'<b>{a_mor[idx]}</b>'
            b_mor[idx] += f'<b>{b_mor[idx]}</b>'
            c_mor[idx] += f'<b>{c_mor[idx]}</b>'
        
        ############################################
        # 마지막 인덱스아니면
        if in_whether_last_idx(idx, a_mor) == False: 
            a_completed += a_mor[idx] + ' '
            b_completed += b_mor[idx] + ' '
            c_completed += c_mor[idx] + ' '

        # 마지막 인덱스이면  
        elif in_whether_last_idx(idx, a_mor) == True:
            a_completed += a_mor[idx]
            b_completed += b_mor[idx]
            c_completed += c_mor[idx]
    
    pre_output_result_list = [a_completed, b_completed, c_completed]
    return pre_output_result_list



def _wrtie_different_component(case_list):
    output_result_list = list() # 결과 물 담을 리스트

    for idx in range(len(case_list)):
        a, b, c = case_list[idx][0], case_list[idx][1], case_list[idx][2]
        a_mor, b_mor, c_mor = _leave_only_words(a), _leave_only_words(b), _leave_only_words(c)
        diff_list = _find_start_stop_idx(a_mor, b_mor, c_mor)
        
        pre_output_result_list = _change_diff_words(a_mor, b_mor, c_mor, diff_list)
        output_result_list.append(pre_output_result_list) # 결과물

    return output_result_list