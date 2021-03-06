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
    sent = re.sub(r'[0-9]{1,}\.[0-9]{1,}(km|m)', '', sent)
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

# Open and create each excel file
workbook = xlsxwriter.Workbook('./mecab_pattern_pdf_'  + timestamp +'.xlsx') 
worksheet = workbook.add_worksheet()

workbook_2 = xlsxwriter.Workbook('./mecab_none_contain_pdf_'  + timestamp +'.xlsx') 
worksheet_2 = workbook_2.add_worksheet()

# 셀 색칠 
cell_yellow = workbook.add_format()
cell_yellow.set_pattern(1)
cell_yellow.set_bg_color('yellow')

# Colum name
worksheet.write('A1', 'Raw')
worksheet.write('B1', 'til english', cell_yellow)
worksheet.write('C1', '패턴', cell_yellow)
worksheet.write('D1', '한글', cell_yellow)
worksheet.write('E1', '한자', cell_yellow)
worksheet.write('F1', '영어', cell_yellow)

worksheet_2.write('A1', '탈락')

wrong_idx = 2
row_idx = 2

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
    
    ko, kot, en = '', '', ''
    # list에서 한글, 한자, 영어 추출해보기
    final_raws = te[0:stop_idx]
    for idx, raw in enumerate(final_raws):
        raw = final_raws[idx][0]
        mor = final_raws[idx][1]
        # 영어
        if mor == 'SL':
            if raw == 'm' or raw == 'km':
                continue
            en = raw
        # 한글, 한자
        else:
            if _isContainKoT(raw) == True:
                if kot == '':
                    kot = raw
                else:
                    kot += raw

            elif _isContainKo(raw) == True:
                if ko == '':
                    ko = raw
                else:
                    ko += raw
    print(ko, kot, en)

    for idx in range(stop_idx):
        key_mor = te[idx][1]
        kokoten += te[idx][0] + ' '
        # print(key_mor)
        if key_mor not in each_te_dict:
            # 바로 더해주기
            each_te_dict[key_mor] = 1
        elif key_mor in each_te_dict:
            each_te_dict[key_mor] += 1

    if len(kokoten) == 0:
        a_idx = _excel_index_creator('A', wrong_idx)
        worksheet_2.write(a_idx, sent)
        wrong_idx += 1

    else:
        if ko == '' or kot == '' or en =='':
            a_idx = _excel_index_creator('A', wrong_idx)
            worksheet_2.write(a_idx, sent)
            wrong_idx += 1
            continue

        a_idx = _excel_index_creator('A', row_idx)
        b_idx = _excel_index_creator('B', row_idx)
        c_idx = _excel_index_creator('C', row_idx)
        d_idx = _excel_index_creator('D', row_idx)
        e_idx = _excel_index_creator('E', row_idx)
        f_idx = _excel_index_creator('F', row_idx)

        # a. raw 쓰기
        worksheet.write(a_idx, reg_sent)

        # b. mecab 쓰기
        te = _start_mecab(reg_sent)
        worksheet.write(b_idx, str(te[0:stop_idx]))

        # c. 패턴쓰기
        worksheet.write(c_idx, kokoten)

        # d. 한글 쓰기
        worksheet.write(d_idx, ko)

        # e. 한자 쓰기
        worksheet.write(e_idx, kot)

        # f. 영어 쓰기
        worksheet.write(f_idx, en)

        row_idx += 1

        

workbook.close()
workbook_2.close()
