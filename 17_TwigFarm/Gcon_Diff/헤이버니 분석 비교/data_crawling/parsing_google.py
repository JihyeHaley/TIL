import timeit
import xlsxwriter
import pandas as pd 

from datetime import datetime

from utils.common_functions import _excel_index_creator
from utils.import_excel import import_ko_df, import_en_hb_df
from utils.crawling_google import google_find_korean
from utils.crawling_papago import papago_find_korean

timestamp = datetime.now().strftime('%m%d%H%M') 

file_name = './data/헤이버니 사전(한-영).xlsx'

# A. 파일 불러오기 
def import_google(file_name):
    # 데이터 import  
    ko_sent_df = import_ko_df(file_name)
    en_hb_df = import_en_hb_df(file_name)
    en_google_final = list()
    en_papago_final = list()
    for idx in range(0, len(ko_sent_df), 500):
        ko_sent_df_range = ko_sent_df[idx: idx + 500]
        # 크롤링
        en_google_df = google_find_korean(idx, ko_sent_df_range)
        for en_google in en_google_df:
            en_google_final.append(en_google)
        
    
        en_papago_df = papago_find_korean(idx, ko_sent_df_range)
        for en_papago in en_papago_df:
            en_papago_final.append(en_papago)

import_google(file_name)
# 엑셀에 쓰기
def write_in_the_excel():
    # A. 파일 불러오기 
    ko_sent_df, en_hb_df, en_google_df, en_papago_df = do_carwling_and_gather(file_name)
    # ko_sent_df, en_hb_df = do_carwling_and_gather(file_name)
    # en_google_df = list()
    # en_papago_df = list()

    # with open('./data/구글 번역본.rtf') as google:
    #     en_google_df = list(google)

    # with open('./data/파파고 번역본.rtf') as papago:
    #     en_papago_df = list(papago)
    print(en_google_df)
    print(en_papago_df)

    workbook = xlsxwriter.Workbook('./results/' + file_name[7:] + '_' + timestamp + '_엑셀.xlsx')

    worksheet = workbook.add_worksheet()

    cell_yellow = workbook.add_format()
    cell_yellow.set_pattern(1)
    cell_yellow.set_bg_color(('yellow'))

    worksheet.write('A1', 'No')
    worksheet.write('B1', '원문', cell_yellow)
    worksheet.write('C1', '헤이버니', cell_yellow)
    worksheet.write('D1', '구글', cell_yellow)
    worksheet.write('E1', '파파고', cell_yellow)
    row_idx = 2
    # 본격적으로 엑셀 쓰기
    for idx in range(len(ko_sent_df)):
        a_idx = _excel_index_creator('A', row_idx)
        b_idx = _excel_index_creator('B', row_idx)
        c_idx = _excel_index_creator('C', row_idx)
        d_idx = _excel_index_creator('D', row_idx)
        e_idx = _excel_index_creator('E', row_idx)

        worksheet.write(a_idx, str(row_idx - 1)) # 인덱스
        worksheet.write(b_idx, str(ko_sent_df[idx])) # 원문
        worksheet.write(c_idx, str(en_hb_df[idx])) # 헤이버니 
        worksheet.write(d_idx, str(en_google_df[idx])) # 구글
        worksheet.write(e_idx, str(en_papago_df[idx])) # 파파고 

        row_idx += 1
    print(f'row_idx : {row_idx}')
    print('done')
    workbook.close()

# write_in_the_excel()