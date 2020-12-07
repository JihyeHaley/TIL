import pandas as pd
import random
import xlsxwriter 


def excel_index_creator(column, row_idx):
    column_idx = column + str(row_idx)
    return column_idx



ko_sample = pd.read_excel('./tagMT_ko_simpl_201201.xlsx_detected.xlsx')
# pre-detect_ko-en, pre-detect_ko-ja
ko_sample_path = ko_sample['path'].tolist()
ko_sample_ko = ko_sample['ko'].tolist()


def ko_en_spliter():
    ###########################
    # 한-영
    ko_sample_en = ko_sample['en'].tolist()
    ko_sample_pro_detect_en = ko_sample['pre-detect_ko-en'].tolist()
    ko_detect_idx = list()
    ko_check_imsi = list()
    
    for _ in range(len(ko_sample_pro_detect_en)):
        detect = ko_sample_pro_detect_en[_]
        if detect == '영어 확인 필요!':
            ko_check_imsi.append(_)
            
    for _ in range(1000):
        check = random.choice(ko_check_imsi)
        ko_detect_idx.append(check)
    
    for __ in range(len(ko_sample_ko)):
        if len(ko_detect_idx) == 1250:
            break
        else:
            comparison = random.choice(ko_sample_ko)
            check_idx = ko_sample_ko.index(comparison)
            if check_idx in ko_detect_idx or ko_sample_pro_detect_en[check_idx] == '영어 확인 필요!':
                continue
            else:
                ko_detect_idx.append(check_idx)
    
    workbook_ko_en = xlsxwriter.Workbook('./tagMT_ko_en_split__'+ '.xlsx')
    worksheet_ko_en = workbook_ko_en.add_worksheet()
    worksheet_ko_en.write('A1', 'path')
    worksheet_ko_en.write('B1', 'no')
    worksheet_ko_en.write('C1', 'ko')
    worksheet_ko_en.write('D1', 'en')
    worksheet_ko_en.write('E1', 'pro-detect_ko_en')
    completed_ko_en = open(f'./ko_en_choice_idx__'+ '.txt', "w+")
    
    row_idx = 2
    for j in ko_detect_idx:
        completed_ko_en.write(str(j)+'\n')
        a_idx = excel_index_creator('A', row_idx)
        worksheet_ko_en.write(a_idx, ko_sample_path[j])

        b_idx = excel_index_creator('B', row_idx)
        no = row_idx - 1
        worksheet_ko_en.write(b_idx, str(no))

        c_idx = excel_index_creator('C', row_idx)
        worksheet_ko_en.write(c_idx,ko_sample_ko[j])

        d_idx = excel_index_creator('D', row_idx)
        worksheet_ko_en.write(d_idx, ko_sample_en[j])


        e_idx = excel_index_creator('E', row_idx)
        detect = ''
        if ko_sample_pro_detect_en[j] == 'nan':
            detect = ''

        elif ko_sample_pro_detect_en[j] == '영어 확인 필요!':
            detect = '영어 확인 필요!'
            
        worksheet_ko_en.write(e_idx, detect)
        
        row_idx += 1
        if row_idx == 1252:
            break
    completed_ko_en.close()
    workbook_ko_en.close() 



def ko_ja_spliter():
    ###########################
    # 한-영
    ko_sample_ja = ko_sample['ja'].tolist()
    ko_sample_pro_detect_ja = ko_sample['pre-detect_ko-ja'].tolist()
    ko_detect_idx = list()
    ko_check_imsi = list()

    for _ in range(len(ko_sample_pro_detect_ja)):
        detect = ko_sample_pro_detect_ja[_]
        if detect == '일본어 확인 필요!':
            ko_check_imsi.append(_)
    
    
    for _ in range(1000):
        check = random.choice(ko_check_imsi)
        ko_detect_idx.append(check)
    
    for __ in range(len(ko_sample_ko)):
        if len(ko_detect_idx) == 1250:
            break
        else:
            comparison = random.choice(ko_sample_ko)
            check_idx = ko_sample_ko.index(comparison)
            if check_idx in ko_detect_idx or ko_sample_pro_detect_ja[check_idx] == '일본어 확인 필요!':
                continue
            else:
                ko_detect_idx.append(check_idx)
    

    workbook_ko_ja = xlsxwriter.Workbook('./tagMT_ko_ja_split__'+ '.xlsx')
    worksheet_ko_ja = workbook_ko_ja.add_worksheet()
    worksheet_ko_ja.write('A1', 'path')
    worksheet_ko_ja.write('B1', 'no')
    worksheet_ko_ja.write('C1', 'ko')
    worksheet_ko_ja.write('D1', 'ja')
    worksheet_ko_ja.write('E1', 'pro-detect_ko_ja')
    completed_ko_ja = open(f'./ko_ja_choice_idx__'+ '.txt', "w+")
    
    row_idx = 2
    for j in ko_detect_idx:
        completed_ko_ja.write(str(j)+'\n')
        a_idx = excel_index_creator('A', row_idx)
        worksheet_ko_ja.write(a_idx, ko_sample_path[j])

        b_idx = excel_index_creator('B', row_idx)
        no = row_idx - 1
        worksheet_ko_ja.write(b_idx, str(no))

        c_idx = excel_index_creator('C', row_idx)
        worksheet_ko_ja.write(c_idx,ko_sample_ko[j])

        d_idx = excel_index_creator('D', row_idx) 
        if ko_sample_ja[j] == '' or ko_sample_ja[j] == 'nan':
            worksheet_ko_ja.write(d_idx, '')
        else:
            worksheet_ko_ja.write(d_idx, str(ko_sample_ja[j]))

        e_idx = excel_index_creator('E', row_idx)
        detect = ''
        if ko_sample_pro_detect_ja[j] == 'nan':
            detect = ''
        elif ko_sample_pro_detect_ja[j] == '일본어 확인 필요!':
            detect = '일본어 확인 필요!'
        worksheet_ko_ja.write(e_idx, detect)
        
        row_idx += 1
        if row_idx == 1252:
            break
    completed_ko_ja.close()
    workbook_ko_ja.close() 


ko_en_spliter()
ko_ja_spliter()