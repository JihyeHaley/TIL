import pandas as pd
import random
import xlsxwriter 


def excel_index_creator(column, row_idx):
    column_idx = column + str(row_idx)
    return column_idx



en_sample = pd.read_excel('./tagMT_en_simpl_201201.xlsx_detected.xlsx')
# pre-detect_ko-en, pre-detect_ko-ja
en_sample_path = en_sample['path'].tolist()
en_sample_en = en_sample['en'].tolist()


def en_ko_spliter():
    ###########################
    # 영-한
    en_sample_ko = en_sample['ko'].tolist()
    en_sample_pro_detect_ko = en_sample['pre-detect_en-ko'].tolist()
    en_detect_idx = list()
    for _ in range(len(en_sample_pro_detect_ko)):
        detect = en_sample_pro_detect_ko[_]
        if detect == '한국어 확인 필요!':
            en_detect_idx.append(_)
    
    for __ in range(len(en_sample_ko)):
        comparison = random.choice(en_sample_ko)
        check_idx = en_sample_ko.index(comparison)
        if check_idx in en_detect_idx:
            continue
        else:
            en_detect_idx.append(check_idx)

    workbook_en_ko = xlsxwriter.Workbook('./tagMT_en_ko_split'+ '.xlsx')
    worksheet_en_ko = workbook_en_ko.add_worksheet()
    worksheet_en_ko.write('A1', 'path')
    worksheet_en_ko.write('B1', 'no')
    worksheet_en_ko.write('C1', 'en')
    worksheet_en_ko.write('D1', 'ko')
    worksheet_en_ko.write('E1', 'pro-detect_en_ko')
    completed_en_ko = open(f'./en_ko_choice_idx'+ '.txt', "w+")
    
    row_idx = 2
    for j in en_detect_idx:
        completed_en_ko.write(str(j)+'\n')
        a_idx = excel_index_creator('A', row_idx)
        worksheet_en_ko.write(a_idx, en_sample_path[j])

        b_idx = excel_index_creator('B', row_idx)
        no = row_idx - 1
        worksheet_en_ko.write(b_idx, str(no))

        c_idx = excel_index_creator('C', row_idx)
        worksheet_en_ko.write(c_idx, str(en_sample_en[j]))

        d_idx = excel_index_creator('D', row_idx)
        worksheet_en_ko.write(d_idx, str(en_sample_ko[j]))


        e_idx = excel_index_creator('E', row_idx)
        detect = ''
        if en_sample_pro_detect_ko[j] == 'nan':
            detect = ''
        elif en_sample_pro_detect_ko[j] == '한국어 확인 필요!':
            detect = '한국어 확인 필요!'
        worksheet_en_ko.write(e_idx, detect)
        
        row_idx += 1
        if row_idx == 3752:
            break
    completed_en_ko.close()
    workbook_en_ko.close() 


def en_ja_spliter():
    ###########################
    # 영-일
    en_sample_ja = en_sample['ja'].tolist()
    
    en_sample_pro_detect_ko = en_sample['pre-detect_en-ja'].tolist()
    en_detect_idx = list()
    for _ in range(len(en_sample_pro_detect_ko)):
        detect = en_sample_pro_detect_ko[_]
        if detect == '일본어 확인 필요!':
            en_detect_idx.append(_)
    print(len(en_detect_idx))
    for __ in range(len(en_sample_ja)):
        comparison = random.choice(en_sample_ja)
        check_idx = en_sample_ja.index(comparison)
        if check_idx in en_detect_idx:
            continue
        else:
            en_detect_idx.append(check_idx)

    print(len(en_detect_idx))
    workbook_en_ja = xlsxwriter.Workbook('./tagMT_en_ja_split'+ '.xlsx')
    worksheet_en_ja = workbook_en_ja.add_worksheet()
    worksheet_en_ja.write('A1', 'path')
    worksheet_en_ja.write('B1', 'no')
    worksheet_en_ja.write('C1', 'en')
    worksheet_en_ja.write('D1', 'ja')
    worksheet_en_ja.write('E1', 'pro-detect_en_ja')
    completed_en_ja = open(f'./en_ja_choice_idx'+ '.txt', "w+")

    row_idx = 2
    for j in en_detect_idx:
        completed_en_ja.write(str(j)+'\n')
        a_idx = excel_index_creator('A', row_idx)
        worksheet_en_ja.write(a_idx, en_sample_path[j])

        b_idx = excel_index_creator('B', row_idx)
        no = row_idx - 1
        worksheet_en_ja.write(b_idx, str(no))

        c_idx = excel_index_creator('C', row_idx)
        worksheet_en_ja.write(c_idx, str(en_sample_en[j]))

        d_idx = excel_index_creator('D', row_idx)
        worksheet_en_ja.write(d_idx, str(en_sample_ja[j]))


        e_idx = excel_index_creator('E', row_idx)
        detect = ''
        if en_sample_pro_detect_ko[j] == 'nan':
            detect = ''
        elif en_sample_pro_detect_ko[j] == '일본어 확인 필요!':
            detect = '일본어 확인 필요!'
        worksheet_en_ja.write(e_idx, detect)
        
        row_idx += 1

        if row_idx == 3752:
            break
    completed_en_ja.close()
    workbook_en_ja.close() 


en_ko_spliter()
en_ja_spliter()