import pandas as pd
import random
import xlsxwriter 


def excel_index_creator(column, row_idx):
    column_idx = column + str(row_idx)
    return column_idx



ja_sample = pd.read_excel('./tagMT_ja_simpl_201201.xlsx_detected.xlsx')
# pre-detect_ko-en, pre-detect_ko-ja
ja_sample_path = ja_sample['path'].tolist()
ja_sample_ja = ja_sample['ja'].tolist()


def ja_ko_spliter():
    ###########################
    # 일-한
    ja_sample_ko = ja_sample['ko'].tolist()
    ja_sample_pro_detect_ko = ja_sample['pre-detect_ja-ko'].tolist()
    ja_detect_idx = list()
    for _ in range(len(ja_sample_pro_detect_ko)):
        ja_detect_idx.append(_)
    random.shuffle(ja_detect_idx)

    workbook_ja_ko = xlsxwriter.Workbook('./tagMT_ja_ko_split'+ '.xlsx')
    worksheet_ja_ko = workbook_ja_ko.add_worksheet()
    worksheet_ja_ko.write('A1', 'path')
    worksheet_ja_ko.write('B1', 'no')
    worksheet_ja_ko.write('C1', 'ja')
    worksheet_ja_ko.write('D1', 'ko')
    worksheet_ja_ko.write('E1', 'pro-detect_ja_ko')

    row_idx = 2
    for j in ja_detect_idx:
        a_idx = excel_index_creator('A', row_idx)
        worksheet_ja_ko.write(a_idx, ja_sample_path[j])

        b_idx = excel_index_creator('B', row_idx)
        no = row_idx - 1
        worksheet_ja_ko.write(b_idx, str(no))

        c_idx = excel_index_creator('C', row_idx)
        worksheet_ja_ko.write(c_idx, str(ja_sample_ja[j]))

        d_idx = excel_index_creator('D', row_idx)
        worksheet_ja_ko.write(d_idx, str(ja_sample_ko[j]))


        e_idx = excel_index_creator('E', row_idx)
        detect = ''
        if ja_sample_pro_detect_ko[j] == 'nan':
            detect = ''
        elif ja_sample_pro_detect_ko[j] == '한국어 확인 필요!':
            detect = '한국어 확인 필요!'
        worksheet_ja_ko.write(e_idx, detect)
        
        row_idx += 1

    workbook_ja_ko.close() 


def ja_en_spliter():
    ###########################
    # 일-영
    ja_sample_en = ja_sample['en'].tolist()
    ja_sample_pro_detect_en = ja_sample['pre-detect_ja-en'].tolist()
    ja_detect_idx = list()
    for _ in range(len(ja_sample_pro_detect_en)):
        ja_detect_idx.append(_)

    random.shuffle(ja_detect_idx)

    workbook_ja_en = xlsxwriter.Workbook('./tagMT_ja_en_split'+ '.xlsx')
    worksheet_ja_en = workbook_ja_en.add_worksheet()
    worksheet_ja_en.write('A1', 'path')
    worksheet_ja_en.write('B1', 'no')
    worksheet_ja_en.write('C1', 'ja')
    worksheet_ja_en.write('D1', 'en')
    worksheet_ja_en.write('E1', 'pro-detect_ja_en')

    row_idx = 2
    for j in ja_detect_idx:
        a_idx = excel_index_creator('A', row_idx)
        worksheet_ja_en.write(a_idx, ja_sample_path[j])

        b_idx = excel_index_creator('B', row_idx)
        no = row_idx - 1
        worksheet_ja_en.write(b_idx, str(no))

        c_idx = excel_index_creator('C', row_idx)
        worksheet_ja_en.write(c_idx, str(ja_sample_ja[j]))

        d_idx = excel_index_creator('D', row_idx)
        worksheet_ja_en.write(d_idx, str(ja_sample_en[j]))


        e_idx = excel_index_creator('E', row_idx)
        detect = ''
        if ja_sample_pro_detect_en[j] == 'nan':
            detect = ''
        elif ja_sample_pro_detect_en[j] == '영어 확인 필요!':
            detect = '영어 확인 필요!'
        worksheet_ja_en.write(e_idx, detect)
        row_idx += 1

    workbook_ja_en.close() 


ja_ko_spliter()
ja_en_spliter()