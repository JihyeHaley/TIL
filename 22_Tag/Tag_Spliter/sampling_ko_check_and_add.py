import pandas as pd
import random
import xlsxwriter 


def excel_index_creator(column, row_idx):
    column_idx = column + str(row_idx)
    return column_idx



ko_ja_undo = pd.read_excel('./검수중_tagMT_ko_ja_choice_1250_민지민_1205_제출.xlsx')
# pre-detect_ko-en, pre-detect_ko-ja
ko_ja_path = ko_ja_undo['path'].tolist()
ko_ja_ko = ko_ja_undo['ko'].tolist()
ko_ja_ja = ko_ja_undo['ja'].tolist()
ko_ja_check = ko_ja_undo['check'].tolist()
ko_ja_duplicated = list()
type_jaja = str(type(ko_ja_ja[0]))
for _ in range(len(ko_ja_ja)):
    try:
        if type(ko_ja_ja[_]) != type_jaja:
            print(f'no:{_} type: {type(ko_ja_ja[_])}\n{ko_ja_ja[_]}')
    except:
        print('no: {_}')
        print(f'type: {type(ko_ja_ja[_])}\n{ko_ja_ja[_]}')
# with open('./ko_ja_duplicated.txt', 'r') as ko_ja_duplciated_txt:
#     for _ in ko_ja_duplciated_txt:
#         ko_ja_duplicated.append(int(_)-2)
# print(ko_ja_duplicated)
# print(len(ko_ja_duplicated))

# ko_ja_unduplicated = list()
# duplicated_cnt = 0
# for _ in range(len(ko_ja_path)):
#     if _ not in ko_ja_duplicated:
#         ko_ja_unduplicated.append(_)
#     elif _ in ko_ja_duplicated:
#         duplicated_cnt += 1
# print(duplicated_cnt)

# workbook_ko_ja = xlsxwriter.Workbook('./tagMT_ko_ja_unduplicated'+ '.xlsx')
# worksheet_ko_ja_check = workbook_ko_ja.add_worksheet()
# worksheet_ko_ja_check.write('A1', 'path')
# worksheet_ko_ja_check.write('B1', 'no')
# worksheet_ko_ja_check.write('C1', 'ko')
# worksheet_ko_ja_check.write('D1', 'ja')
# worksheet_ko_ja_check.write('E1', 'chcek')
    
# row_idx = 2


# for idx in ko_ja_unduplicated:
    
#     a_idx = excel_index_creator('A', row_idx)
#     worksheet_ko_ja_check.write(a_idx, str(ko_ja_path[idx]))
    

#     b_idx = excel_index_creator('B', row_idx)
#     no = row_idx - 1
#     worksheet_ko_ja_check.write(b_idx, str(no))

#     c_idx = excel_index_creator('C', row_idx)
#     worksheet_ko_ja_check.write(c_idx, str(ko_ja_ko[idx]))
#     # # print(f'{row_idx}: {ko_ja_ko[idx]}')

#     # d_idx = excel_index_creator('D', row_idx)
#     # try:
#     #     ja = str(ko_ja_ja[idx])
#     #     worksheet_ko_ja_check.write(d_idx, ja)
#     # except:
#     #     worksheet_ko_ja_check.write(d_idx, '')

#     e_idx = excel_index_creator('E', row_idx)
#     detect = ''
#     if ko_ja_check[idx] == '' or ko_ja_check[idx] == 'nan':
#         detect = ''
#     elif ko_ja_check[idx] == '검토필요':
#         detect ='검토필요'
#     worksheet_ko_ja_check.write(e_idx, str(detect))
#     row_idx += 1
    
# print(row_idx)
# workbook_ko_ja.close()








            
    



    

        




