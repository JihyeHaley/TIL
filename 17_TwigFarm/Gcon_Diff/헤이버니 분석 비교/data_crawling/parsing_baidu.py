import timeit
import xlsxwriter
import pandas as pd 

from datetime import datetime

from utils.common_functions import _excel_index_creator
from utils.import_excel import import_ko_df, import_en_hb_df
from utils.crawling_baidu import baidu_find_korean

timestamp = datetime.now().strftime('%m%d%H%M') 

file_name = './data/헤이버니 사전(한-영).xlsx'

# A. 파일 불러오기 
def import_google(file_name):
    # 데이터 import  
    ko_sent_df = import_ko_df(file_name)
    en_hb_df = import_en_hb_df(file_name)
    en_baidu_final = list()
    for idx in range(0, len(ko_sent_df), 500):
        ko_sent_df_range = ko_sent_df[idx: idx + 500]
        # 크롤링
        en_baidu_df = baidu_find_korean(idx, ko_sent_df_range)
        for en_baidu in en_baidu_df:
            en_baidu_final.append(en_baidu)

import_google(file_name)
