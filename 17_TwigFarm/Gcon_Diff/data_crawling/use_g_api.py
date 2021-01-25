import time

import pandas as pd

from googletrans import Translator
translator = Translator()

translated = translator.translate('안녕하세요',dest='en')
print(translated.origin)
print(translated.text)ß

xlsxFile = './1_엑셀.xlsx'

df = pd.read_excel(xlsxFile)
ko_sent_df = df['관형'].tolist()

def find_korean(ko_sent_df):

    for ko_sent in ko_sent_df:
        # 3. 입력하기
        print(translator.translate('hello').text)
        
        

find_korean(ko_sent_df)