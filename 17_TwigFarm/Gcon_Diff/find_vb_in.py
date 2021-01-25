import timeit
import nltk

from datetime import datetime
from nltk.corpus import stopwords 
from tensorflow.keras.preprocessing.text import text_to_word_sequence

from mor_check import in_whether_last_idx, in_start_tokenizer, in_words_change, in_vb_in_connect

# 단어만 가져오기
def _filter_leave_only_words(sent):
    words_list, mor_list, words_mor_list = in_start_tokenizer(sent) # 형태소 분석 nltk tokenizer
    checked_words_list, checked_mor_list = in_vb_in_connect(words_list, mor_list, words_mor_list) # 동사 + 전치사 해결하기
    # if len(checked_words_list) != len(checked_mor_list):
        # print('not same')
    return checked_words_list, checked_mor_list


# find what is different components in the sentence
def _find_diff_word_idx(a_words, b_words, c_words):
    diff_idx = 0 # 인덱스 
    diff_word_idx_list = list() # 인덱스 리스트 초기화

    for idx in range(len(a_words)):
        if a_words[idx] != b_words[idx] or a_words[idx] != c_words[idx] or b_words[idx] != c_words[idx]:
            diff_idx = idx
        else: 
            continue
        diff_word_idx_list.append(diff_idx)

    return diff_word_idx_list


# <b> 를 slicing 해서 더해주기
def in_add_and_completed(sent, words_list, diff_idx):
    words_list[diff_idx] = f'<b>{words_list[diff_idx]}</b>'    
    return words_list 


# 슬라이싱 해서 <b>하고 문장완성
def _make_full_sent_using_slicing_words(a, b, c, a_words, b_words, c_words, diff_list):
    pre_output_result_list = list() # 초기화
    
    for diff_idx in diff_list:
        a_words = in_add_and_completed(a, a_words, diff_idx)
        b_words = in_add_and_completed(b, b_words, diff_idx)
        c_words = in_add_and_completed(c, c_words, diff_idx)

    a_completed, b_completed, c_completed = '', '', ''

    for jdx in range(len(a_words)):
        a_first_word, b_first_word, c_first_word = '', '', ''

        if jdx == 0:
            a_first_letter = a.split(' ')[0][0] # 첫 단 대문자 처리 
            b_first_letter = b.split(' ')[0][0] # 원래 문장 ' '로 잘라서 가장 첫 문장으로 넣어주기
            c_first_letter = c.split(' ')[0][0]
            
            if a_words[jdx] != b_words[jdx] or b_words[jdx] != c_words[jdx] or a_words[jdx] != c_words[jdx]:
                print('_case_if')
                a_completed += f'<b>{a_first_letter}{a_words[jdx][4:]}'
                b_completed += f'<b>{b_first_letter}{b_words[jdx][4:]}'
                c_completed += f'<b>{c_first_letter}{c_words[jdx][4:]}'
                
            else: 
                print('_case_else')
                a_completed += f'{a_first_letter}{a_words[jdx][1:]}'
                b_completed += f'{b_first_letter}{b_words[jdx][1:]}'
                c_completed += f'{c_first_letter}{c_words[jdx][1:]}'
                

        # 마지막 인덱스는 띄어 쓰기 없이 만나기
        elif jdx == len(a_words) - 1:
            a_completed += a_words[jdx]
            b_completed += b_words[jdx]
            c_completed += c_words[jdx]

        else:
            # 띄어쓰기
            a_completed += ' ' + a_words[jdx]
            b_completed += ' ' + b_words[jdx]
            c_completed += ' ' + c_words[jdx]


    pre_output_result_list = [a_completed, b_completed, c_completed]
    print(pre_output_result_list)
    print('#'*40)
    return pre_output_result_list


# 결론문
def _wrtie_different_component(case_list):
    # [[1_1문장, 1_2문장, 1_3문장], [2_1문장, 2_2문장, 2_3문장], ......]
    output_result_list = list() # 결과 물 담을 리스트
    output_mor_list = list() # 결과 물 담을 리스트
    output_diff_times_list = list()
    # 
    for idx in range(len(case_list)):
        
        a, b, c = case_list[idx][0], case_list[idx][1], case_list[idx][2]
        a_words, a_mor = _filter_leave_only_words(a)
        b_words, b_mor = _filter_leave_only_words(b)
        c_words, c_mor = _filter_leave_only_words(c)
    
        diff_word_idx_list = _find_diff_word_idx(a_words, b_words, c_words)
        pre_output_result_list = _make_full_sent_using_slicing_words(a, b, c, a_words, b_words, c_words, diff_word_idx_list)
       
        output_result_list.append(pre_output_result_list) # 결과물
        pre_output_mor_list = [a_mor, b_mor, c_mor]
        output_mor_list.append(pre_output_mor_list)
        output_diff_times_list.append(len(diff_word_idx_list))

    return output_result_list, output_mor_list, output_diff_times_list