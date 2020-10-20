from sents import *
from regex import * 
import xlsxwriter

def raw_sents_preprocessing():
    topic = str(input('어떤 주제의 파일을 list로 만들고 싶어요?'))
    with open(f'/Users/jihyeoh/Desktop/NIA_NER/ NIA_DICT/{topic}_raw_input.txt', 'r') as raw_sents:
        raw_sents = raw_sents.readlines()
        # raw_sentences = [print(idx, _.strip('\n')) for idx, _ in enumerate(raw_sentences)]
        raw_sents = [_.strip('\n') for _ in raw_sents]
    return raw_sents

raw_sents = raw_sents_preprocessing()

def output(raw_sents):
    topic = str(input('어떤 주제의 파일을 excel로 만들고 싶어요?'))
    workbook = xlsxwriter.Workbook(f'/Users/jihyeoh/desktop/NIA_NER/ NIA_DICT/{topic}_raw_ko_en' + '.xlsx')
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

output(raw_sents)