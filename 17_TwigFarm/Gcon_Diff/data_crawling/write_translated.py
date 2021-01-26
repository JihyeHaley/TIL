import timeit
import xlsxwriter
from datetime import datetime

from utils import excel_index_creator, in_docx_to_raw_text
from use_bs4_google import google_find_korean
from use_bs4_papago import papago_find_korean
from original import import_ko_df, import_google_df, import_papago_df

timestamp = datetime.now().strftime('%m%d%H%M') 

# 엑셀에 쓰기
def write_in_the_excel():
    ko_sent_df = import_ko_df()
    en_google_sent_df = import_google_df()
    en_papago_sent_df = import_papago_df()
    # en_google_sent_df = google_find_korean() # 구글 크롤링
    # en_papago_sent_df = papago_find_korean() # 파파고 크롤링
    print(ko_sent_df)
    print(en_google_sent_df)
    print(en_papago_sent_df)

    workbook = xlsxwriter.Workbook('./관형_구글_파파고_번역포함_' + timestamp + '_엑셀.xlsx')

    worksheet = workbook.add_worksheet()

    cell_yellow = workbook.add_format()
    cell_yellow.set_pattern(1)
    cell_yellow.set_bg_color(('yellow'))

    worksheet.write('A1', 'No')
    worksheet.write('B1', '관형', cell_yellow)
    worksheet.write('C1', '구글', cell_yellow)
    worksheet.write('D1', '파파고', cell_yellow)


    row_idx = 2
    for idx in range(len(ko_sent_df)):
        a_idx = excel_index_creator('A', row_idx)
        b_idx = excel_index_creator('B', row_idx)
        c_idx = excel_index_creator('C', row_idx)
        d_idx = excel_index_creator('D', row_idx)

        worksheet.write(a_idx, str(row_idx - 1)) # 인덱스
        worksheet.write(b_idx, str(ko_sent_df[idx])) # 한글 - 원본
        worksheet.write(c_idx, str(en_google_sent_df[idx])) # 구글 - 영어 번역본
        worksheet.write(d_idx, str(en_papago_sent_df[idx])) # 파파고 - 영어 번역본
        row_idx += 1

    print(f'row_idx : {row_idx}')
    print('done')
    workbook.close()

write_in_the_excel()