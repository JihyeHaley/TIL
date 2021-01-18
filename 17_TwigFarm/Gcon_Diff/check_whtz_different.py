import re
import timeit

from konlpy.tag import Mecab
from datetime import datetime

from input_source import xlsx_to_list

# import and save as list
# file_name, case_list = xlsx_to_list()
# output_result_list = list()

# 형태소 분석
def _start_mecab(sent):
    m = Mecab()
    mor_list = m.pos(sent)
    ''' te -> list > tuple > str'''
    return mor_list

# 앞 글자만 가져오기
def _leave_only_words(mor_list):
    words_list = list()
    for mor_tuple in mor_list:
        words_list.append(mor_tuple[0])
    return words_list


# 마지막 인덱스인지 체크
def _whether_last_idx(idx, words_list):
    length = len(any_list)
    if idx == length - 1:
        return True
    elif idx != length - 1:
        return False
    

# find what is different components in the sentence
def _find_start_stop_idx(a_splited, b_splited, c_splited):
    start_idx, stop_idx = 0, 0
    cnt = 0
    for idx in range(len(a_splited)):
        print(f'idx: {idx}\n')
        if a_splited[idx] == b_splited[idx] == c_splited[idx]:
            if cnt == 1:
                stop_idx = idx
            continue
        else: 
            cnt += 1
            if cnt == 1: # cnt=0 이면, 달라지는 첫 시작
                start_idx = idx
                print('here 1')
        print(f'cnt: {cnt}\n')
               
        
    print(start_idx, stop_idx)
    return start_idx, stop_idx


# <b> 넣어서 리턴해주기
def _return_diff_words(a_splited, b_splited, c_splited, start_idx, stop_idx):
    if start_idx == stop_idx:
        a_diff = f'<b>{a_splited[start_idx]}</b>'
        b_diff = f'<b>{b_splited[start_idx]}</b>'
        c_diff = f'<b>{c_splited[start_idx]}</b>'
    elif start_idx != stop_idx:
        a_diff = f'<b>{b_splited[start_idx:][0]}</b>'
        b_diff = f'<b>{b_splited[start_idx:][0]}</b>'
        c_diff = f'<b>{c_splited[start_idx:][0]}</b>'
    return a_diff, b_diff, c_diff


case_list = ['I am SunHo.', 'I am SeonHo.', 'I am Sunnoo.'] # I, am, Sunho
def _wrtie_different_component(case_list):
    a, b, c = case_list[0], case_list[1], case_list[2] # 문장
    print(a)
    a_splited, b_splited, c_splited = a.split(' '), b.split(' '), c.split(' ') # 단어로 쪼개

    start_idx, stop_idx = _find_start_stop_idx(a_splited, b_splited, c_splited)
    
    a_diff, b_diff, c_diff = _return_diff_words(a_splited, b_splited, c_splited, start_idx, stop_idx)
    a_same, b_same, c_same = '', '', ''

    for idx in range(start_idx):
        if idx == 0:
            a_same = a_splited[idx] + ' '
            b_same = b_splited[idx] + ' '
            c_same = c_splited[idx] + ' '
        else:
            a_same = a_same + a_splited[idx] + ' '
            b_same = b_same + b_splited[idx] + ' '
            c_same = c_same + c_splited[idx] + ' '

    a_completed = a_same + a_diff
    b_completed = b_same + b_diff
    c_completed = c_same + c_diff

    output_result_list = [a_completed, b_completed, c_completed]
    return output_result_list

print(_wrtie_different_component(case_list))

# def return_to_output_source():
#     return file_name, output_result_list