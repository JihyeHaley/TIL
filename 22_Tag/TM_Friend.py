from raw_data_to_list import call_tagMT_ko_simple_lan
from konlpy.tag import Mecab
mecab = Mecab()

# test용으로 simple의 한글 먼저 받아와서 돌리기
ko_list = call_tagMT_ko_simple_lan('ko')
for _ in ko_list:
    print(mecab.pos(_))
