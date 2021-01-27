import pandas as pd

def import_df():
    xlsxFile = '헤이버니 사전(한-영).xlsx_01271737_엑셀.xlsx'
    df = pd.read_excel(xlsxFile)
    ko_df = df['원문'].tolist()
    google_df = df['구글'].tolist()
    papago_df = df['파파고'].tolist()
    return ko_df, google_df, papago_df
