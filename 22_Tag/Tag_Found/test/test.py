# from konlpy.tag import Mecab

# mecab = Mecab()
# sent = '안녕하세요, 지혜입니다.'
# sent = mecab.pos(sent)

import pandas as pd
tm_raw_data = pd.read_excel('./tagMT_ko_simpl.xlsx')
ko_list = tm_raw_data['ko'].tolist()
en_list = tm_raw_data['en'].tolist()
ja_list = tm_raw_data['ja'].tolist()

for _ in ko_list:
    print(_, '\n')
# print(raw_data['ko'].tolist())