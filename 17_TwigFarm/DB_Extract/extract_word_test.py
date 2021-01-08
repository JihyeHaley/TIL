from datetime import datetime
import re
import xlsxwriter
import pandas as pd
import timeit

from word_pos_test import _start_mecab 
from pdf_utils import _isContainKo, _isContainKoT, _isContainEn, _read_pdf_to_text

## excel idx 
def _excel_index_creator(colum, row_idx):
    colum_idx = colum + str(row_idx)
    return colum_idx


xlsx_file = './한국하천지명사전_1월_8일.xlsx'

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
worksheet.write('C1', 'mor count', cell_yellow)
worksheet.write('D1', 'Ko Kot En', cell_yellow)

worksheet_2.write('A1', '탈락')
wrong_idx = 2
row_idx = 2

# analyze and write
for idx, sent in enumerate(raw_data):
    output_sent = re.sub(r'▶', '', sent)
    output_sent = re.sub(r'[0-9]{1,}\.[0-9]{1,}km', '', output_sent)
    te = _start_mecab(output_sent)
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
    
    print(stop_idx)                    
    
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
        a_idx = _excel_index_creator('A', row_idx)
        b_idx = _excel_index_creator('B', row_idx)
        c_idx = _excel_index_creator('C', row_idx)
        d_idx = _excel_index_creator('D', row_idx)

        print(output_sent)
        # a. raw 쓰기
        worksheet.write(a_idx, output_sent)

        # b. mecab 쓰기
        te = _start_mecab(output_sent)
        worksheet.write(b_idx, str(te[0:stop_idx]))

        # c. pattern 쓰기
        worksheet.write(c_idx, str(each_te_dict))

        # d. pattern 쓰기
        worksheet.write(d_idx, kokoten)


        row_idx += 1

    

workbook.close()
workbook_2.close()
