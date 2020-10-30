import os
import xlsxwriter
from check_pattern import *


## sentence 전처리 갖고놀기 #############################################################
def raw_sents_preprocessing():
    with open('/Users/jihyeoh/Desktop/NIA_NER/NIA_DICT/의약학_raw_input.txt', 'r') as raw_sents:
        raw_sents = raw_sents.readlines()
        # raw_sentences = [print(idx, _.strip('\n')) for idx, _ in enumerate(raw_sentences)]
        raw_sents = [_.strip('\n') for _ in raw_sents]
    return raw_sents


# 전처리 갖고놀기
raw_sents = raw_sents_preprocessing()


for raw_sent in raw_sents:
    word_matched = find_pattern_show_words(raw_sent)