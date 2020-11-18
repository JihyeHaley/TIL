import re
import os
from raw_data_to_list import call_tagMT_ko_simple_lan
from konlpy.tag import Mecab
import xlsxwriter
from datetime import datetime
import timeit


timestamp = datetime.now().strftime('%m%d%H%M')
workbook = xlsxwriter.Workbook('./regex_test_' + timestamp + '_.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1' , 'Raw TM')
worksheet.write('B1' , 'Reg Tag')


mecab = Mecab()
# test용으로 simple의 한글 먼저 받아와서 돌리기
ko_list = call_tagMT_ko_simple_lan('ko')

for _ in ko_list:
    