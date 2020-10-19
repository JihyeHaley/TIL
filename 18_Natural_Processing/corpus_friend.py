import os
import xlsxwriter
from words import *
from regex import *

###############################################################
######sentence
# sentence 처음쓰기 새로쓰기
def raw_sents_input_new():
    n = int(input('문장을 몇번 입력 받으실래요? '))
    print('단어를 더이상 입력하기 싫으면 0을 눌러주세요')
    new_sents_log = open(f'./raw_input.txt', 'w')
    for i in range(n):
        if i == 0:
            print(f'sample로 {n}개만 먼저 input받습니다.')
        print(f'{str(i+1)}/{n}개')
        a = str(input('Input your sent: '))
        if a == '0':
            break
        sentence = a + '\n'
        new_sents_log.write(sentence)
    new_sents_log.close()  



def raw_sents_input_append():
    n = int(input('문장을 몇번 입력 받으실래요? '))
    print('단어를 더이상 입력하기 싫으면 0을 눌러주세요')
    append_sent_log = open(f'./01_raw_sentence_input_collecting.txt', 'a')
    
    for i in range(n):
        print(f'{str(i+1)}/{n}개')
        a = str(input('Input your sent: '))
        if a == '0':
            break
        sentence = a + '\n'
        append_sent_log.write(sentence)
    append_sent_log.close()  



# sentence 전처리 갖고놀기
def raw_sents_preprocessing():
    with open('./01_raw_sentence_input_collecting.txt', 'r') as raw_sents:
        raw_sents = raw_sents.readlines()
        # raw_sentences = [print(idx, _.strip('\n')) for idx, _ in enumerate(raw_sentences)]
        raw_sents = [_.strip('\n') for _ in raw_sents]
    return raw_sents



## sent 실행 함수#############################################################
# 처음쓰기 새로쓰기
# raw_sents_input_new()

# 이어쓰기
# raw_sents_input_append()


# 전처리 갖고놀기
raw_sents = raw_sents_preprocessing()
out_raw_sents = [print(idx, _.strip('\n')) for idx, _ in enumerate(raw_sents)]


for idx, sent in enumerate(raw_sents):
    sent = find_English(sent)
    print(idx, sent)

for idx, sent in enumerate(raw_sents):
    rabbit = find_pattern(sent)
    print(rabbit)

## word 실행 함수#############################################################
# 처음쓰기 새로쓰기
# raw_words_input_new()

# 이어쓰기
# raw_words_input_append()

# 전처리 갖고놀기
# raw_words = raw_words_preprocessing()
# print(len(raw_words))


## 엑셀 #############################################################
workbook = xlsxwriter.Workbook('/Users/jihyeoh/desktop/GIT/TIL/18_Natural_Processing/01_raw_sent_input_collecting' + '.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'Raw Data')
worksheet.write('B1', 'KOR')
worksheet.write('C1', 'KOR')
row_idx = 2
for raw_sent in raw_sents:
    idx = 'A' + str(row_idx)
    worksheet.write(idx, raw_sent)
    row_idx += 1
workbook.close()
