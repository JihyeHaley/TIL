import openpyxl
import pandas as pd
import xlsxwriter


def excel_index_creator(colum, row_idx):
    colum_idx = colum + str(row_idx)
    return colum_idx

# 한/영
or_xlsxFile = './일본어_파싱_데이터/이노룰스 사전모음 (한,영)/5-3. InnoRules 7.2메시지_한영-TM.xlsx'
df = pd.read_excel(or_xlsxFile)
or_ko = df['ko'].tolist()
or_en = df['en'].tolist()
print(f'or_len: {len(or_ko)}')

# 파싱된 한/일
pr_xlsxFile = './result_5_1_ko_jp_.xlsx'
df = pd.read_excel(pr_xlsxFile)
pr_ko = df['ko'].tolist()
pr_jp = df['jp'].tolist()
print(f'pr_ko: {len(pr_ko)}')

# 파싱한 한/일, dict로 편하게 보기 한:일
pr_ko_jp_dict = dict()
for i in range(len(pr_ko)):
    pr_ko_jp_dict[pr_ko[i]] = pr_jp[i] 

workbook = xlsxwriter.Workbook('./worked_5_3_ko_en_jp_.xlsx') 
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'ko')
worksheet.write('B1', 'en')
worksheet.write('C1', 'jp')
row_idx = 2

# pandas를 이용하여 각 시트별 데이터 가져오기
for idx, raw in enumerate(or_ko):
    ko = or_ko[idx]
    en = or_en[idx]

    # a_idx 작성 (ko)
    a_idx = excel_index_creator('A', row_idx)
    worksheet.write(a_idx, str(ko))
    
    # b_idx 작성 (en)
    b_idx = excel_index_creator('B', row_idx)
    worksheet.write(b_idx, str(en))

    # c_idx 작성 (jp)
    c_idx = excel_index_creator('C', row_idx)
    for key, value in pr_ko_jp_dict.items():
        if ko == key:
            worksheet.write(c_idx, str(value))
        else:
            worksheet.write(c_idx, '')

    row_idx += 1
    print(row_idx)
    
workbook.close()