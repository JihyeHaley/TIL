import time

import pandas as pd

#  1. 관형 가져오기
def import_ko_df():
    xlsxFile = './관형_구글번역포함_01261205_엑셀.xlsx'
    df = pd.read_excel(xlsxFile)
    ko_sent_df = df['관형'].tolist()
    return ko_sent_df

#  1. 구글번역본 가져오기
def import_google_df():
    xlsxFile = './관형_구글번역포함_01261205_엑셀.xlsx'
    df = pd.read_excel(xlsxFile)
    en_google_sent_df = df['구글'].tolist()
    return en_google_sent_df

#  1. 파파고번역본 가져오기
def import_papago_df():
    xlsxFile = './관형_구글번역포함_01261205_엑셀.xlsx'
    df = pd.read_excel(xlsxFile)
    en_google_sent_df = df['파파고'].tolist()
    return en_google_sent_df

