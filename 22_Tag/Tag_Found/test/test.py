from raw_data_to_list import call_tagMT_ko_simple_lan
from konlpy.tag import Mecab
import xlsxwriter
from datetime import datetime
import timeit


timestamp = datetime.now().strftime('%m%d%H%M')
workbook = xlsxwriter.Workbook('./test_' + timestamp + '_.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1' , 'Raw TM')
worksheet.write('B1' , 'Pos Tag')

row_idx = 2


# 엑셀 인덱스 작업
def excel_index_creator(column, row_idx):
    column_idx = column + str(row_idx)
    return column_idx


mecab = Mecab()
# test용으로 simple의 한글 먼저 받아와서 돌리기
ko_list = call_tagMT_ko_simple_lan('ko')
for _ in ko_list:
    a_idx = excel_index_creator('A', row_idx)
    worksheet.write(a_idx, _)

    b_idx = excel_index_creator('B', row_idx)
    pos = str(mecab.pos(_))
    worksheet.write(b_idx, pos)
    
    row_idx += 1
    
workbook.close()