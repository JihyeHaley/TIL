import pandas as pd

def _import_df():
    ko_xlsxFile = '헤이버니 사전(한-영).xlsx'
    ko_df = pd.read_excel(ko_xlsxFile)
    ko_all = ko_df['ko'].tolist()
    
    # return ko_original_df, google_df, papago_df
    return ko_all