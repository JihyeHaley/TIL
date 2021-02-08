import timeit
import xlsxwriter
import pandas as pd 

from datetime import datetime

from utils.common_functions import _excel_index_creator
from utils.import_excel_kakao import import_ko_df
from utils.crawling_kakao import kakao_find_korean

timestamp = datetime.now().strftime('%m%d%H%M') 

file_name = './data/헤이버니 사전(한-영).xlsx'

ko_sent_df = import_ko_df(file_name)

# kakao_find_korean(ko_sent_df[:1000]) # 완료
# kakao_find_korean(ko_sent_df[1000:2000]) # 완료
# kakao_find_korean(ko_sent_df[2000:3000])
kakao_find_korean(ko_sent_df[3000:])

