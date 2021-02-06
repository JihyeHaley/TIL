import pandas as pd

def import_df():
    en_xlsxFile = '구글_파파고_3000.xlsx'
    en_df = pd.read_excel(en_xlsxFile)
    google_df = en_df['구글'].tolist()[:3000]
    papago_df = en_df['파파고'].tolist()[:3000]

    ko_xlsxFile = '헤이버니 사전(한-영).xlsx'
    ko_df = pd.read_excel(ko_xlsxFile)
    ko_all = ko_df['ko'].tolist()[:3000]
    
    return ko_all, google_df, papago_df
