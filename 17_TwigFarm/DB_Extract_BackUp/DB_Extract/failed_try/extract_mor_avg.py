from datetime import datetime
import re
import xlsxwriter
import pandas as pd
import timeit

from word_pos_test import _start_mecab 
from pdf_utils import _isContainKo, _isContainKoT, _isContainEn, _read_pdf_to_text

def _reg_sent(sent):
    # 특수기호는 빼기
    sent = re.sub(r'▶', '', sent)
    # _,_._km
    sent = re.sub(r'[0-9]{0,},[0-9]{1,}\.[0-9]{1,}km', '', sent)
    return sent

## excel idx 
def _excel_index_creator(colum, row_idx):
    colum_idx = colum + str(row_idx)
    return colum_idx


xlsx_file = './한국하천지명사전_1월_8일_all.xlsx'

timestamp = datetime.now().strftime('%m%d%H%M')
start = timeit.default_timer()

df = pd.read_excel(xlsx_file)   
raw_data = df['Raw'].tolist()

total_mor_dict = dict()
cnt = 0
# analyze and write
for idx, sent in enumerate(raw_data):
    reg_sent = _reg_sent(sent)
    te = _start_mecab(reg_sent)

    ''' te -> list > tuple > str'''
    te_len = len(te)
    # ko, kot, en
    each_te_dict = dict()
    stop_idx = 0
    kokoten = ''
    for idx, mor in enumerate(te):
        if mor[1] == 'SL':
            for _ in range(idx, te_len):
                if te[_][1] != 'SL':
                    stop_idx = _
                    break

    for idx in range(stop_idx):
        key_mor = te[idx][1]
        kokoten += te[idx][0] + ' '
        # print(key_mor)
        if key_mor not in each_te_dict:
            # 바로 더해주기
            each_te_dict[key_mor] = 1
        elif key_mor in each_te_dict:
            each_te_dict[key_mor] += 1

    # total_mor_dict 에 넣어줘서 전체 평균 구해보기
    print(te[0:stop_idx])
    for idx, _ in enumerate(te[0:stop_idx]):
        if _[1] not in total_mor_dict:
            total_mor_dict[_[1]] = 1
        elif _[1] in total_mor_dict:
            total_mor_dict[_[1]] += 1
    cnt += 1

print(f'total_mor_dict: {total_mor_dict}')
print(f'cnt: {cnt}')

for key, value in total_mor_dict.items():
    print(f'{key}_avg: {round(value/cnt, 2)}')