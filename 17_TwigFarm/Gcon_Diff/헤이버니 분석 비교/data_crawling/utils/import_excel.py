import time

import pandas as pd


# file_name = '4000_rest.xlsx'


# 헤이버니 ko import 
def import_ko_df(file_name):
    df = pd.read_excel(file_name)
    ko_sent_df = df['rest'].tolist()
    return ko_sent_df



