import openpyxl
import pandas as pd
import xlsxwriter


def excel_index_creator(colum, row_idx):
    colum_idx = colum + str(row_idx)
    return colum_idx



xlsxFile = './일본어_파싱_데이터/이노룰스 번역본 문서 (일본어)/5.2 & 5.3 InnoRules 7.2 화면 Message&Caption.xlsx'

# openpyxl를 이용하여 시트명 가져오기
sheetList = ['MESSAGES', 'CAPTIONS', 'ENV_EXPLANATIONS']

ko_en_dict = dict()
workbook = xlsxwriter.Workbook('./result_5_2_3_ko_jp_.xlsx') 
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'ko')
worksheet.write('B1', 'jp')
row_idx = 2

# pandas를 이용하여 각 시트별 데이터 가져오기
xlsx = pd.ExcelFile(xlsxFile)
for j in sheetList:
    df = pd.read_excel(xlsx, j)
    print('%s Sheet의 데이타 입니다.' %j)
    ko_raw = df['KOR'].tolist()
    jp_raw = df['JPN'].tolist()
    ko = []
    jp = []

    for i in range(len(ko_raw)):
        if ko_raw[i] == '':
            continue
        ko.append(ko_raw[i])
        jp.append(jp_raw[i])
            
    if len(ko) == len(jp):
        for idx in range(len(ko)):
            if ko[idx] == '' or jp[idx] == '':
                continue
            
            # dict에 담아주기
            ko_en_dict[ko[idx]] = jp[idx]

            # a_idx 작성
            a_idx = excel_index_creator('A', row_idx)
            worksheet.write(a_idx, str(ko[idx]))

            # b_idx 작성
            b_idx = excel_index_creator('B', row_idx)
            worksheet.write(b_idx, str(jp[idx]))

            row_idx += 1
            
    print(ko_en_dict)
    print('*' * 50)
    
workbook.close()