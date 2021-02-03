import timeit
import xlsxwriter

import pandas as pd

from datetime import datetime

from similarity import calc_distance
from import_excel import import_df
from common_functions import _excel_index_creator
from mor_analyze import _work_start_tokenizer
from dark_check import _diff_word_dark
timestamp = datetime.now().strftime('%m%d%H%M') 


# data 가져오기
def _data_import():
    ko_df, google_df, papago_df = import_df()
    return ko_df, google_df, papago_df


# 유사도 측정
def _check_similarity(idx, ko_df, google_words, papago_words):
    similarity_price = list()
    #실행 예
    samples = [google_words, papago_words]
    base = samples[0] # 구글 중심
    r = sorted(samples, key = lambda n: calc_distance(base, n)) #base(신촌역)과 samples의 각 원소 비교
    for n in r:
        similarity_price.append(calc_distance(base, n))
        # print(calc_distance(base, n), n)
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
    
    row_idx = 2
    # 본격적으로 엑셀 쓰기

    for idx in range(len(google_df)):
        # 형태소
        google_words, google_mor = _work_start_tokenizer(google_df[idx])
        papago_words, papago_mor = _work_start_tokenizer(papago_df[idx])
        similarity_price = _check_similarity(idx, ko_df, google_words, papago_words)
        a_idx = _excel_index_creator('A', row_idx)
        b_idx = _excel_index_creator('B', row_idx)
        c_idx = _excel_index_creator('C', row_idx)
        d_idx = _excel_index_creator('D', row_idx)
    
        print(google_df[idx])
        print(papago_df[idx])
        worksheet.write(a_idx, str(ko_df[idx])) # c. 원문
        worksheet.write(c_idx, str(similarity_price[-1])) # c. 유사도
        if similarity_price[-1] >= 9 or similarity_price[-1] == 0 or len(google_words) <= 3 or len(papago_words) <= 3:
            worksheet.write(b_idx, str(google_df[idx])) # 구글
            worksheet.write(d_idx, str(papago_df[idx])) # 파파고 
        
        elif similarity_price[-1] > 0 and similarity_price[-1] < 9:
            g_sent, p_sent = _diff_word_dark(google_words, papago_words)
            worksheet.write(b_idx, str(g_sent), cell_yellow) # 구글
            worksheet.write(d_idx, str(p_sent), cell_yellow) # 파파고 
            print(g_sent)
            print(p_sent)
        row_idx += 1
    print(f'row_idx : {row_idx}')
    print('done')
    workbook.close()

write_in_the_excel()
