import time

import pandas as pd

from googletrans import Translator
translator = Translator()

# translated = translator.translate('hello', dest='en', src='ko')
# print('1')
# print(translated.origin)
# print('2')
# print(translated.text)

xlsxFile = './1_엑셀.xlsx'

df = pd.read_excel(xlsxFile)
ko_sent_df = df['관형'].tolist()

def find_korean(ko_sent_df):

    for ko_sent in ko_sent_df:
        # 3. 입력하기
        print(translator.translate(str('hello'), dest='en', src='ko').text)
        
        

find_korean(ko_sent_df)