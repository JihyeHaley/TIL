import pandas as pd

def import_df():
    en_xlsxFile = '헤이버니_구글_파파고_1000.xlsx'
    en_df = pd.read_excel(en_xlsxFile)
    google_df = en_df['구글'].tolist()
    papago_df = en_df['파파고'].tolist()

    ko_xlsxFile = '헤이버니 사전(한-영).xlsx'
    ko_df = pd.read_excel(ko_xlsxFile)
    ko_all = ko_df['ko'].tolist()[823:]
    ko_original_df = list()
    for idx in range(500):
        ko_original_df.append(ko_all[idx])

    for idx in range(500, 1001):
        ko_original_df.append(ko_all[idx])

    return ko_original_df, google_df, papago_df


