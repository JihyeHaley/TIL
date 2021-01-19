import re
import timeit
import nltk


from konlpy.tag import Mecab
from datetime import datetime

nltk.download('punkt')

# 형태소 분석 mecab
def in_start_mecab(sent):
    m = Mecab()
    mor_list = m.pos(sent)
    ''' te -> list > tuple > str'''
    return mor_list


# 형태소 분석 nltk tokenizer
def in_start_nltk_tokenizer(sent):
    words_list = nltk.tokenize.word_tokenize(sent)
    mor_list = nltk.tag.pos_tag(words_list)
    return words_list, mor_list


# 마지막 인덱스인지 체크
def in_whether_last_idx(idx, words_list):
    length = len(words_list)
    if idx == length - 1:
        return True
    elif idx != length - 1:
        return False


# 앞 글자만 가져오기
def _leave_only_words(sent):
    # mor_list = in_start_mecab(sent) # 형태소 분석 mecab
    words_list, mor_list = in_start_nltk_tokenizer(sent) # 형태소 분석 nltk tokenizer
    return words_list, mor_list


# find what is different components in the sentence
def _find_start_stop_idx(a_words, b_words, c_words):
    diff_idx = 0 # 인덱스 
    diff_list = list() # 인덱스 리스트 초기화
    for idx in range(len(a_words)):
        if a_words[idx] == b_words[idx] == c_words[idx]:
            continue
        else: 
            diff_idx = idx
        diff_list.append(diff_idx)
           
    return diff_list



# <b> 넣어주면서 글쓰기 change diff words
def _change_diff_words(a, b, c, a_mor, b_mor, c_mor, diff_list):
    a_completed, b_completed, c_completed = '', '', '' 
    pre_output_result_list = list() # 초기화
    for idx in range(len(a_mor)):
        # change words with tag
        if idx in diff_list:
            a_mor[idx] = f'<b>{a_mor[idx]}</b>'
            b_mor[idx] = f'<b>{b_mor[idx]}</b>'
            c_mor[idx] = f'<b>{c_mor[idx]}</b>'
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


# <b> 를 slicing 해서 더해주기
def in_add_and_completed(sent, words_list, diff_idx):
    completed_sent = ''
    find_start = 0
    print(sent)
    for jdx in range(diff_idx):
        find_start += len(words_list[jdx])
    if find_start + len(words_list[diff_idx]) * 2 < len(sent):
        if len(words_list[diff_idx]) <= 2:
            find_last = len(sent)
        else:
            find_last = find_start + len(words_list[diff_idx]) * 2
    elif find_start + len(words_list[diff_idx]) * 2 > len(sent):
        find_last = len(sent)
    
    print('find_start - ', find_start, '/', len(sent) )
    print('find_last - ', find_last,  '/', len(sent) )

    for kdx in range(find_start, find_last):
        if sent[kdx:kdx + len(words_list[diff_idx])] == words_list[diff_idx]:
            head = sent[:kdx]
            tail = sent[kdx + len(words_list[diff_idx]):]
            middle = f'<b>{words_list[diff_idx]}</b>'
            completed_sent = head + middle + tail
            # print(head, tail, middle)
    return completed_sent 


# 슬라이싱 해서 <b>하고 문장완성
def _make_full_sent_using_slicing_words(a, b, c, a_words, b_words, c_words, diff_list):
    a_completed, b_completed, c_completed = '', '', '' 
    pre_output_result_list = list() # 초기화
    
    for idx, diff_idx in enumerate(diff_list):
        print(idx, '-', diff_idx)
        if idx == 0:
            a_completed = in_add_and_completed(a, a_words, diff_idx)
            b_completed = in_add_and_completed(b, b_words, diff_idx)
            c_completed = in_add_and_completed(c, c_words, diff_idx)
        elif idx > 0:
            a_completed = in_add_and_completed(a_completed, a_words, diff_idx)
            b_completed = in_add_and_completed(b_completed, b_words, diff_idx)
            c_completed = in_add_and_completed(c_completed, c_words, diff_idx)
        
        print(a_completed, b_completed, c_completed)

    pre_output_result_list = [a_completed, b_completed, c_completed]
    return pre_output_result_list


# 결론문
def _wrtie_different_component(case_list):
    output_result_list = list() # 결과 물 담을 리스트
    output_mor_list = list() # 결과 물 담을 리스트

    for idx in range(len(case_list)):
        a, b, c = case_list[idx][0], case_list[idx][1], case_list[idx][2]
        a_words, a_mor = _leave_only_words(a)
        b_words, b_mor = _leave_only_words(b)
        c_words, c_mor = _leave_only_words(c)
        print(a_mor)
        print(b_mor)
        print(c_mor)
        diff_list = _find_start_stop_idx(a_words, b_words, c_words)
        
        pre_output_result_list = _make_full_sent_using_slicing_words(a, b, c, a_words, b_words, c_words, diff_list)
        output_result_list.append(pre_output_result_list) # 결과물
        pre_output_mor_list = [a_mor, b_mor, c_mor]
        output_mor_list.append(pre_output_mor_list)

    return output_result_list, output_mor_list