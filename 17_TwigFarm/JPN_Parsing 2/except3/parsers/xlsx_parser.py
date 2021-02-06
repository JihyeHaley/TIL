"""
    excel parser
"""
import os
from datetime import datetime
import timeit
import pandas as pd
import xlsxwriter

from utils.common_functions import *
from utils.regex_functions import *

def _excel_index_creator(colum, row_idx):
    colum_idx = colum + str(row_idx)
    return colum_idx


def xlsx_to_excel(xlsx_files, sub_path):
    if len(xlsx_files) == 0:
        print('''-----------------------------------------------------------
        XLSX파일 없습니다.
        ''')
    else:
        print('''-----------------------------------------------------------
        EXCEL 작업 시작합니다.
        ''')
        timestamp = datetime.now().strftime("%m%d%H%M")
        print(" Total excels: ", len(xlsx_files))

        start = timeit.default_timer()
        
        for xlsx_file in xlsx_files:
            file_name =  xlsx_file.split('/')[-1]
            workbook = xlsxwriter.Workbook('./results/일본어_빈칸_영어_' + file_name + '.xlsx')
            worksheet = workbook.add_worksheet()

            cell_yellow = workbook.add_format()
            cell_yellow.set_pattern(1)
            cell_yellow.set_bg_color(('yellow'))

            sky_blue = workbook.add_format()
            sky_blue.set_pattern(1)
            sky_blue.set_bg_color(('blue'))

            worksheet.write('A1', 'ko', cell_yellow)
            worksheet.write('B1', 'en', cell_yellow)
            worksheet.write('C1', 'jp', cell_yellow)
            row_idx = 2 


            df = pd.read_excel(xlsx_file)
            ko_df = df['ko'].tolist()
            en_df = df['en'].tolist()
            jp_df = df['jp'].tolist()
            print(f'ko-{len(ko_df)}, en-{len(en_df)}, jp-{len(jp_df)}')
            which_idx  = list()

            for idx in range(len(jp_df)):
                a_idx = _excel_index_creator('A', row_idx)
                b_idx = _excel_index_creator('B', row_idx)
                c_idx = _excel_index_creator('C', row_idx)

                worksheet.write(a_idx, str(ko_df[idx])) # A. 
                worksheet.write(b_idx, str(en_df[idx])) # B. 

                if jp_df[idx] == 'its_empty_cell':
                    # empty하다면, 영어 넣어주기
                    worksheet.write(c_idx, str(en_df[idx]), sky_blue) # C. 영어넣기
                    which_idx.append(idx)
                else:
                    worksheet.write(c_idx, str(jp_df[idx])) # C. 원래 일본어 넣기
                row_idx += 1
            print(f'{xlsx_file} : {which_idx}')
            print('#'*40)
            workbook.close()

        stop = timeit.default_timer()

        print(" ----> Raw excel to excel DONE (Running Time: ", stop - start, " sec.)")