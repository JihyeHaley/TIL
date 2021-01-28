import timeit
import xlsxwriter

import pandas as pd

from datetime import datetime

from similarity import calc_distance
from import_excel import import_df
from common_functions import _excel_index_creator

timestamp = datetime.now().strftime('%m%d%H%M') 


# data 가져오기
def _data_import():
    ko_df, google_df, papago_df = import_df()
    return ko_df, google_df, papago_df


# 유사도 측정
def _check_similarity(idx, ko_df, google_df, papago_df):
    similarity_price = list()
    #실행 예
    samples = [google_df[idx], papago_df[idx]]
    base = samples[0] # 구글 중심
    r = sorted(samples, key = lambda n: calc_distance(base, n)) #base(신촌역)과 samples의 각 원소 비교
    for n in r:
        similarity_price.append(calc_distance(base, n))
        print(calc_distance(base, n), n)
    return similarity_price



# 엑셀에 쓰기
def write_in_the_excel():
    # A. 파일 불러오기 
    ko_df, google_df, papago_df = _data_import()
    
    workbook = xlsxwriter.Workbook('./results/' +  '_' + timestamp + '_엑셀.xlsx')

    worksheet = workbook.add_worksheet()

    cell_yellow = workbook.add_format()
    cell_yellow.set_pattern(1)
    cell_yellow.set_bg_color(('yellow'))

    worksheet.write('A1', 'No')
    worksheet.write('B1', '구글', cell_yellow)
    worksheet.write('C1', '유사도', cell_yellow)
    worksheet.write('D1', '파파고', cell_yellow)
    worksheet.write('E1', '구글_형태소', cell_yellow)
    worksheet.write('F1', '파파고_형태소', cell_yellow)
    row_idx = 2
    # 본격적으로 엑셀 쓰기

    for idx in range(len(google_df)):
        similarity_price = _check_similarity(idx, ko_df, google_df, papago_df)
       
        a_idx = _excel_index_creator('A', row_idx)
        b_idx = _excel_index_creator('B', row_idx)
        c_idx = _excel_index_creator('C', row_idx)
        d_idx = _excel_index_creator('D', row_idx)
        d_idx = _excel_index_creator('E', row_idx)
        d_idx = _excel_index_creator('F', row_idx)

        worksheet.write(a_idx, str(ko_df[idx])) # 원문
        worksheet.write(b_idx, str(google_df[idx])) # 구글
        worksheet.write(c_idx, str(similarity_price[-1])) # 유사도
        worksheet.write(d_idx, str(papago_df[idx])) # 파파고 
        worksheet.write(d_idx, ) # 구글 형태소 
        worksheet.write(d_idx, ) # 파파고 형태소

        row_idx += 1
    print(f'row_idx : {row_idx}')
    print('done')
    workbook.close()

write_in_the_excel()
