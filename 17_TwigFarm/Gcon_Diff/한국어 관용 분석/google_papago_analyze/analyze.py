import xlsxwriter
import pandas as pd

from datetime import datetime

from data_import import import_ko_df, import_google_df, import_papago_df
from utils import _show_mor

timestamp = datetime.now().strftime('%m%d%H%M') # time stamp

# excel index
def excel_index_creator(colum, row_idx):
    colum_idx = colum + str(row_idx)
    return colum_idx


# 한국어, 영어 가져고기
def _import_ens():
    ko_list = import_ko_df()
    en_google_list = import_google_df()
    en_papago_list = import_papago_df()

    return ko_list, en_google_list, en_papago_list


def _upper(word):
    word = word.strip(' ')
    word = word.upper()
    return word

# 데이터 가져오기
ko_list, en_google_list, en_papago_list = _import_ens()


# 비슷하면 same으로
def _check_whether_same(en_google_list, en_papago_list):
    check_diff = list()
    for idx in range(len(en_google_list)):
        google_upper, papago_upper = _upper(en_google_list[idx]), _upper(en_papago_list[idx])

        if _upper(en_google_list[idx]) == _upper(en_papago_list[idx]):
            check_diff.append('same')
        # 조금이라도 포함이 되면
        elif google_upper in papago_upper or papago_upper in google_upper:
            check_diff.append('same')
        elif _upper(en_google_list[idx]) != _upper(en_papago_list[idx]):
            check_diff.append('diffs')

    return check_diff

check_diff = _check_whether_same(en_google_list, en_papago_list)

workbook = xlsxwriter.Workbook('./google_papago_compare_' + timestamp + '_.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'no')
worksheet.write('B1', 'google_mor')
worksheet.write('C1', 'google')
worksheet.write('D1', 'diff')
worksheet.write('E1', 'papago')
worksheet.write('F1', 'papago_mor')
row_idx = 2

for idx in range(len(en_google_list)):
    a_idx = excel_index_creator('A', row_idx)
    b_idx = excel_index_creator('B', row_idx)
    c_idx = excel_index_creator('C', row_idx)
    d_idx = excel_index_creator('D', row_idx)
    e_idx = excel_index_creator('E', row_idx)
    f_idx = excel_index_creator('F', row_idx)

    google_words, google_words_mors, papago_words, papag_words_mors = _show_mor(idx, en_google_list, en_papago_list)
    print(idx)
    worksheet.write(a_idx, str(row_idx - 1))
    worksheet.write(b_idx, str(google_words_mors))
    worksheet.write(c_idx, en_google_list[idx])
    worksheet.write(d_idx, check_diff[idx])
    worksheet.write(e_idx, en_papago_list[idx])
    worksheet.write(f_idx, str(papag_words_mors))
    row_idx += 1

workbook.close()


# df = pd.DataFrame([en_google_list, check_diff, en_papago_list],
#                   columns=['google', 'diff', 'papago'])

# df.to_excel('./google_papago_compar.xlsx', sheet_name='compare')