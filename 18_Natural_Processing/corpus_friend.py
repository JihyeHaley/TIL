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

# 전처리 갖고놀기
# raw_words = raw_words_preprocessing()
# print(len(raw_words))


## sentence 전처리 갖고놀기 #############################################################
def raw_sents_preprocessing():
    with open(f'./공학_raw_sentence_input_collecting.txt', 'r') as raw_sents:
        raw_sents = raw_sents.readlines()
        # raw_sentences = [print(idx, _.strip('\n')) for idx, _ in enumerate(raw_sentences)]
        raw_sents = [_.strip('\n') for _ in raw_sents]
    return raw_sents


## sent 입력받기 실행 함수###############################################################
# 처음쓰기 새로쓰기
# raw_sents_input_new()

# 이어쓰기
# raw_sents_input_append()


# 전처리 갖고놀기
raw_sents = raw_sents_preprocessing()
# out_raw_sents = [print(idx, _.strip('\n')) for idx, _ in enumerate(raw_sents)]

## excel idx 함수
def excel_index_creator(colum, row_idx):
    colum_idx = colum + str(row_idx)
    return colum_idx

## 엑셀 ###############################################################################
workbook = xlsxwriter.Workbook('./before_reporting' + '.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'Raw Data')
worksheet.write('B1', 'KOR')
worksheet.write('C1', 'ENG')
row_idx = 2

for idx, sent in enumerate(raw_sents):
    en_words = find_En(sent)
    ko_words = find_Ko(sent)
    print(idx, sent)
    a_idx = excel_index_creator('A', row_idx)
    worksheet.write(a_idx, sent)
    for j in range(len(ko_words)):
        b_idx = excel_index_creator('B', row_idx)
        c_idx = excel_index_creator('C', row_idx)
        worksheet.write(b_idx, ko_words[j])
        worksheet.write(c_idx, en_words[j])
        row_idx += 1
workbook.close()






