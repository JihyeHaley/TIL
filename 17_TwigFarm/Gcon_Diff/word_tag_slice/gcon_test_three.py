import xlsxwriter
import nltk

from tensorflow.keras.preprocessing.text import text_to_word_sequence
import pandas as pd

def _import_df():
    file_name = './data/구글_파파고_카카오.xlsx'
    df = pd.read_excel(file_name)
    ko_df = df['원문'].tolist()[:1000]
    g_df = df['구글'].tolist()[:1000]
    p_df = df['파파고'].tolist()[:1000]
    k_df = df['카카오'].tolist()[:1000]
    
    return ko_df, g_df, p_df, k_df


# a. search_length
def _find_search_length(A, B, C):
    min_length = [A, B, C]
    search_length = min(map(len, min_length))
    return search_length


# b. idx, <b>, </b>
def _find_different(A, B, C):
    search_length = _find_search_length(A, B, C)
    print(A)
    print(B)
    print(C)
    a_start_idx, b_start_idx, c_start_idx = 0, 0 ,0

    for idx in range(search_length):
        a, b, c = A[idx], B[idx], C[idx]
        if a != b or b != c or a != c:
            A[idx] = '<b>' + a
            B[idx] = '<b>' + b
            C[idx] = '<b>' + c
            a_start_idx, b_start_idx, c_start_idx = idx, idx, idx
            break

    for idx in range(1, search_length + 1):
        a, b, c = A[-idx], B[-idx], C[-idx]
        print(-idx)
        if a != b or b != c or a != c:
            A[-idx] = f'{a}</b>'
            B[-idx] = f'{b}</b>'
            C[-idx] = f'{c}</b>'
            break

    return A, B, C, a_start_idx, b_start_idx, c_start_idx


# c. connect_word, find start & end idx
def _make_sentence(G, start_idx):
    s = ''
    s_start_idx, s_end_idx = 0, 0

    for idx, a in enumerate(G):
        if idx == start_idx:
            s_start_idx = len(s)

        if idx <= len(G) - 1:
            s += a + ' '
        elif idx == len(G) - 1:
            s += a

    for jdx in range(0, len(s) - 4):
        if s[jdx:jdx+4] == '</b>':
            s_end_idx = jdx + 4
    
    return s, s_start_idx, s_end_idx

# 형태소 분석 nltk tokenizer
def _work_start_tokenizer(sent):
    # 단어만 남기기
    # words_list = text_to_word_sequence(sent) # [Hi, My, name, is, jihye] (문장의 첫 단어도 )
    words_list_pre = sent.split(' ') # space bar로 단어 쪼개기 훨씬 더 정확할 것 같음
    words_list = list()

    for word in words_list_pre:
        if word != '':
            words_list.append(word)

    # 단어와 형태소 List
    words_mor_list = nltk.tag.pos_tag(words_list) # [(Hi, NNG), ...] 
    return words_list


def _make_sentence(A, start_idx):
    s = ''
    s_start_idx, s_end_idx = 0, 0

    for idx, a in enumerate(A):
        if idx == start_idx:
            s_start_idx = len(s)

        if idx <= len(A) - 1:
            s += a + ' '
        elif idx == len(A) - 1:
            s += a

    for jdx in range(0, len(s) - 4):
        if s[jdx:jdx+4] == '</b>':
            s_end_idx = jdx + 4
    
    return s, s_start_idx, s_end_idx

def workwork():
    ko_df, g_df, p_df, k_df = _import_df()
    
    for idx, ko_sent in enumerate(ko_df):
        print(idx + 1)
        print(ko_sent)  

        google_words = _work_start_tokenizer(g_df[idx]) # 구글
        papago_words = _work_start_tokenizer(p_df[idx]) # 파파고
        kakao_words = _work_start_tokenizer(k_df[idx]) # 파파고
        
        google_words, papago_words, kakao_words, g_start_idx, p_start_idx, k_start_idx = _find_different(google_words, papago_words, kakao_words)
        
        g, g_start_idx, g_end_idx = _make_sentence(google_words, g_start_idx)
        p, p_start_idx, p_end_idx = _make_sentence(papago_words, p_start_idx)
        k, k_start_idx, k_end_idx = _make_sentence(kakao_words, k_start_idx)

        print(g, g_start_idx, g_end_idx)
        print(p, p_start_idx, p_end_idx)
        print(k, k_start_idx, k_end_idx)            
        
workwork()