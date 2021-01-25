import timeit
import nltk

from datetime import datetime
from nltk.corpus import stopwords 
from tensorflow.keras.preprocessing.text import text_to_word_sequence

from utils.work_connect_funcs import _work_start_tokenizer, _work_vb_in_connect, _work_connet_change, _work_add_and_completed, _work_connect_word

# A. leave only words and filter verb and in in the word_list from sent
def _let_only_import_words_from_sent(sent):
    # 1.
    words_list, mor_list, words_mor_list = _work_start_tokenizer(sent) # 형태소 분석 nltk tokenizer
    # 2, 3.
    checked_words_list, checked_mor_list = _work_vb_in_connect(words_list, mor_list, words_mor_list) # 동사 + 전치사 해결하기

    return checked_words_list, checked_mor_list


# B. find what is different components in the each sentence
def _let_find_diff_word_idx(a_words, b_words, c_words):
    diff_idx = int() # show diff_idx is number 
    diff_word_idx_list = list() # clear all components (for safety)

    for idx in range(len(a_words)):
        # if all three components are not equal, add the index to the diff_idx_list
        if a_words[idx] != b_words[idx] or a_words[idx] != c_words[idx] or b_words[idx] != c_words[idx]:
            diff_idx = idx
        else: 
            continue
        diff_word_idx_list.append(diff_idx)

    return diff_word_idx_list



# C. 슬라이싱 해서 <b>하고 문장완성
def _let_make_full_sent_using_slicing(a, b, c, a_words, b_words, c_words, diff_list):
    pre_output_result_list = list() # 초기화
    
    for diff_idx in diff_list:
        # 4.
        a_words = _work_add_and_completed(a, a_words, diff_idx)
        b_words = _work_add_and_completed(b, b_words, diff_idx)
        c_words = _work_add_and_completed(c, c_words, diff_idx)

    # 5. 
    pre_output_result_list = _work_connect_word(a_words, b_words, c_words, a, b, c)
    
    return pre_output_result_list


# 결론문
def _wrtie_different_component(case_list):
    # [[1_1문장, 1_2문장, 1_3문장], [2_1문장, 2_2문장, 2_3문장], ......]
    output_result_list = list() # 결과 물 담을 리스트
    output_mor_list = list() # 결과 물 담을 리스트
    output_diff_times_list = list()
    # 
    for idx in range(len(case_list)):
        ############################
        # A.
        a, b, c = case_list[idx][0], case_list[idx][1], case_list[idx][2]
        a_words, a_mor = _let_only_import_words_from_sent(a)
        b_words, b_mor = _let_only_import_words_from_sent(b)
        c_words, c_mor = _let_only_import_words_from_sent(c)
        
        ############################
        # B.
        diff_word_idx_list = _let_find_diff_word_idx(a_words, b_words, c_words)
        
        ############################
        #C.
        pre_output_result_list = _let_make_full_sent_using_slicing(a, b, c, a_words, b_words, c_words, diff_word_idx_list)
       
        output_result_list.append(pre_output_result_list) # 결과물
        pre_output_mor_list = [a_mor, b_mor, c_mor]
        output_mor_list.append(pre_output_mor_list)
        output_diff_times_list.append(len(diff_word_idx_list))

    return output_result_list, output_mor_list, output_diff_times_list