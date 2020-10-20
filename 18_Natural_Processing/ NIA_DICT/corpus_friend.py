import os
import xlsxwriter
from words import *
from regex import *
from sents import *

## word 실행 함수##### ###############################################################
# 처음쓰기 새로쓰기
# raw_words_input_new()

# 이어쓰기
# raw_words_input_append()



## sent 입력받기 실행 함수###############################################################
# 입력받기
raw_sents_input_append()


## sentence 전처리 갖고놀기 #############################################################
def raw_sents_preprocessing():
    with open('./NIA_NER/ NIA_DICT/공학_raw_sentence_input_collecting.txt', 'r') as raw_sents:
        raw_sents = raw_sents.readlines()
        # raw_sentences = [print(idx, _.strip('\n')) for idx, _ in enumerate(raw_sentences)]
        raw_sents = [_.strip('\n') for _ in raw_sents]
    return raw_sents


# 전처리 갖고놀기
# raw_sents = raw_sents_preprocessing()
# out_raw_sents = [print(idx, _.strip('\n')) for idx, _ in enumerate(raw_sents)]


## 엑셀 ###############################################################################
def output(raw_sents):
    workbook = xlsxwriter.Workbook('./NIA_NER/ NIA_DICT/공학_raw_ko_en' + '.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', 'Raw Data')
    worksheet.write('B1', 'KOR')
    worksheet.write('C1', 'ENG')
    row_idx = 2

    for idx, sent in enumerate(raw_sents):
        en_words, en_words_len = find_En(sent)
        ko_words = find_Ko(sent, en_words_len)
        print(idx, sent, en_words, ko_words)
        a_idx = 'A' + str(row_idx)
        worksheet.write(a_idx, sent)
        for j in range(len(ko_words)):
            b_idx = 'B' + str(row_idx)
            c_idx = 'C' + str(row_idx)
            worksheet.write(b_idx, ko_words[j])
            worksheet.write(c_idx, en_words[j])
            row_idx += 1
    workbook.close()

## 작업 다 한 후 엑셀파일로 내보내기   
# output(raw_sents)






