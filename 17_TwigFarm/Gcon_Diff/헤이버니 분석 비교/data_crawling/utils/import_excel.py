import time

import pandas as pd


file_name = '헤이버니 사전(한-영).xlsx'


# 헤이버니 koimport 
def import_ko_df(file_name):
    df = pd.read_excel(file_name)
    ko_sent_df = df['ko'].tolist()[2001:3001]
    return ko_sent_df


# 헤이버니 en import 
def import_en_hb_df(file_name):
    df = pd.read_excel(file_name)
    en_hb_df = df['en'].tolist()[2001:3001]
    return en_hb_df



