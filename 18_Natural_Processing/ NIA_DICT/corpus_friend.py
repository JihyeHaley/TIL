import os
import xlsxwriter
from words import *
from regex import *
from sents import *
from mecab import *


## word 실행 함수##### ###############################################################
# 처음쓰기 새로쓰기
# raw_words_input_new()

# 이어쓰기
# raw_words_input_append()



## sent 입력받기 실행 함수###############################################################
# 입력받기
# raw_sents_input_append()


## sentence 전처리 갖고놀기 #############################################################
def raw_sents_preprocessing():
    with open('/Users/jihyeoh/Desktop/NIA_NER/NIA_DICT/의약학_raw_input.txt', 'r') as raw_sents:
        raw_sents = raw_sents.readlines()
        # raw_sentences = [print(idx, _.strip('\n')) for idx, _ in enumerate(raw_sentences)]
        raw_sents = [_.strip('\n') for _ in raw_sents]
    return raw_sents


# 전처리 갖고놀기
raw_sents = raw_sents_preprocessing()
print(raw_sents)
# out_raw_sents = [print(idx, _.strip('\n')) for idx, _ in enumerate(raw_sents)]

for raw_sent in raw_sents:
    word_matched = find_pattern_show_words(raw_sent)

## excel idx 
def excel_index_creator(colum, row_idx):
    colum_idx = colum + str(row_idx)
    return colum_idx


# wecab.py
## 엑셀 ###############################################################################
def mecab_output(raw_sents):
    workbook = xlsxwriter.Workbook('/Users/jihyeoh/Desktop/GIT/TIL/18_Natural_Processing/ NIA_DICT/의약학_raw_ko_en_wecab4_mustbessossc_ETN_1' + '.xlsx') # _mustbessossc
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', 'Raw Sent')
    worksheet.write('B1', 'KOR')
    worksheet.write('C1', 'ENG')
    worksheet.write('D1', 'MOR')
    worksheet.write('E1', '매캡')

    row_idx = 2

    for idx, raw_sent in enumerate(raw_sents):
        # A. Raw Sent 쓰기
        a_idx =excel_index_creator('A', row_idx)
        worksheet.write(a_idx, raw_sent)
        print('A확인', raw_sent)

        # raw _sent 형태소 분석 시작
        te, word_matched, mor_match_list_str = find_pattern_show_words(raw_sent)
        print(word_matched)
        
        # Raw Sent에 대한 수술 후 뽑혀진 한-영 짝꿍들
        ko_words, en_words = make_str(word_matched)
        print(ko_words, en_words)

        # E. 쓰기
        e_idx =excel_index_creator('E', row_idx)
        worksheet.write(e_idx, te)
        print('E확인')

        for j in range(len(ko_words)):
            # B.  ko_word 쓰기
            b_idx =excel_index_creator('B', row_idx)
            worksheet.write(b_idx, ko_words[j])

            # C.  en_word 쓰기
            c_idx = excel_index_creator('C', row_idx)
            worksheet.write(c_idx, en_words[j])


            # D.  en_word 쓰기
            d_idx = excel_index_creator('D', row_idx)
            print(idx, raw_sent, '\n\t', ko_words[j], '-', en_words[j])
            # 한-영 짝꿍이 안 맞으면 엑셀에 아예 raw_sent도 입력이 안되서 
            # length가 다를때는 일단 넘어가고 
            if len(ko_words) != len(mor_match_list_str):
                continue
            # length가 같을때는 쓰게 만들기
            worksheet.write(d_idx, mor_match_list_str[j])

            row_idx += 1

    workbook.close()
## 작업 다 한 후 엑셀파일로 내보내기   
mecab_output(raw_sents)

# regex.py
## 엑셀 ###############################################################################
def regex_output(raw_sents):
    workbook = xlsxwriter.Workbook('./NIA_NER/NIA_DICT/공학_raw_ko_en' + '.xlsx')
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
# regex_output(raw_sents)






