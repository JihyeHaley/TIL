import time

import pandas as pd

#  1. 관형 가져오기
def import_ko_df(file_name):
    
    df = pd.read_excel(file_name)
    ko_sent_df = df['관형'].tolist()
    return ko_sent_df

#  1. 구글번역본 가져오기
def import_google_df(file_name):
    
    df = pd.read_excel(file_name)
    en_google_sent_df = df['구글'].tolist()
    return en_google_sent_df

#  1. 파파고번역본 가져오기
def import_papago_df(file_name):

    df = pd.read_excel(file_name)
    en_google_sent_df = df['파파고'].tolist()
    return en_google_sent_df

