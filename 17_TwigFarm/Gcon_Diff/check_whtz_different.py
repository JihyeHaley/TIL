import re
import timeit

from konlpy.tag import Mecab
from datetime import datetime

from input_source import xlsx_to_list


# 형태소 분석
def _start_mecab(sent):
    m = Mecab()
    mor_list = m.pos(sent)
    ''' te -> list > tuple > str'''
    return mor_list


# 앞 글자만 가져오기
def _leave_only_words(sent):
    mor_list = _start_mecab(sent)
    words_list = list()
    for mor_tuple in mor_list:
        words_list.append(mor_tuple[0])
    return words_list


# 마지막 인덱스인지 체크
def _whether_last_idx(idx, words_list):
    length = len(words_list)
    if idx == length - 1:
        return True
    elif idx != length - 1:
        return False
    

# find what is different components in the sentence
def _find_start_stop_idx(a_mor, b_mor, c_mor):
    diff_idx = 0
    diff_list = list()
    for idx in range(len(a_mor)):
        if a_mor[idx] == b_mor[idx] == c_mor[idx]:
            continue
        else: 
            diff_idx = idx
        diff_list.append(diff_idx)
           
        
    return diff_list


# <b> 넣어서 리턴해주기
def _return_diff_words(a_mor, b_mor, c_mor, diff_list):
    for diff_idx in diff_list:
        a_mor[diff_idx] = f'<b>{a_mor[diff_idx]}</b>'
        b_mor[diff_idx] = f'<b>{b_mor[diff_idx]}</b>'
        c_mor[diff_idx] = f'<b>{c_mor[diff_idx]}</b>'
    a_completed, b_completed, c_completed = '', '', ''
    
    for idx in range(len(a_mor)):
        if idx < len(a_mor) - 1:
            if idx == diff_idx:
                a_completed += a_mor[idx]
                b_completed += b_mor[idx]
                c_completed += c_mor[idx]
            else:
                a_completed += a_mor[idx] + ' '
                b_completed += b_mor[idx] + ' '
                c_completed += c_mor[idx] + ' '
        else:
            a_completed += a_mor[idx]
            b_completed += b_mor[idx]
            c_completed += c_mor[idx]
    
    output_group_list = [a_completed, b_completed, c_completed]
    
    return output_group_list



def _wrtie_different_component():
    # import and save as list
    file_name, case_list = xlsx_to_list()
    output_result_list = list()

    for idx in range(len(case_list)):
        a, b, c = case_list[idx][0], case_list[idx][1], case_list[idx][2]
        a_mor, b_mor, c_mor = _leave_only_words(a), _leave_only_words(b), _leave_only_words(c)
        diff_list = _find_start_stop_idx(a_mor, b_mor, c_mor)
        
        output_group_list = _return_diff_words(a_mor, b_mor, c_mor, diff_list)
        output_result_list.append(output_group_list)

    return file_name, case_list, output_result_list