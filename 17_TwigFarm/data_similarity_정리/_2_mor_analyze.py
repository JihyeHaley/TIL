'''
    문장에서 단어를 형태소 분석을 통해서 -> [단어] or [단어, 형태소]기기
'''

import nltk
from tensorflow.keras.preprocessing.text import text_to_word_sequence

# 형태소 분석 nltk tokenizer
def _work_start_tokenizer(sent):
    # 단어만 남기기
    words_list = text_to_word_sequence(sent) # [Hi, My, name, is, jihye] (문장의 첫 단어도 )

    # 단어와 형태소 List
    words_mor_list = nltk.tag.pos_tag(words_list) # [(Hi, NNG), ...] 

    return words_list, words_mor_list