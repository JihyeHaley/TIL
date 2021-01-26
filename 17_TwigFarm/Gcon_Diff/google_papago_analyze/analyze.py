import xlsxwriter

import pandas as pd

from data_import import import_ko_df, import_google_df, import_papago_df


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


def _lower(word):
    word = word.strip(' ')
    word = word.lower()
    return word

# 데이터 가져오기
ko_list, en_google_list, en_papago_list = _import_ens()

check_diff = list()

for idx in range(len(en_google_list)):
    if _lower(en_google_list[idx]) == _lower(en_papago_list[idx]):
        check_diff.append('same')
    else:
        check_diff.append('diffs')

print(len(en_google_list))
print(len(check_diff))
print(len(en_papago_list))

workbook = xlsxwriter.Workbook('./google_papago_compare.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'no')
worksheet.write('B1', 'google')
worksheet.write('C1', 'diff')
worksheet.write('D1', 'papago')
row_idx = 2

for idx in range(len(en_google_list)):
    a_idx = excel_index_creator('A', row_idx)
    b_idx = excel_index_creator('B', row_idx)
    c_idx = excel_index_creator('C', row_idx)
    d_idx = excel_index_creator('D', row_idx)

    worksheet.write(a_idx, str(row_idx - 1))
    worksheet.write(b_idx, en_google_list[idx])
    worksheet.write(c_idx, check_diff[idx])
    worksheet.write(d_idx, en_papago_list[idx])
    row_idx += 1

workbook.close()


# df = pd.DataFrame([en_google_list, check_diff, en_papago_list],
#                   columns=['google', 'diff', 'papago'])

# df.to_excel('./google_papago_compar.xlsx', sheet_name='compare')