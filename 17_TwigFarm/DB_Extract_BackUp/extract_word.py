'''
    pdf parser
'''

from datetime import datetime
import timeit
import xlsxwriter
from tqdm import tqdm
from read_pdf import read_pdf_to_text
import re
import pandas as pd



# 한국어
def _isContainKo(text):
    ko = re.compile(r'.*[가-힇ㄱ-ㅎㅏ-ㅣ]+') 
    # return bool(ko.fullmatch(text))
    return bool(ko.match(text))  


# 한자
def _isContainKoT(text):
    kot = re.compile(r'.*[一-龥]+') 
    # return bool(ko.fullmatch(text))
    return bool(kot.match(text))   


# 영어
def _isContainEn(text):
    en = re.compile(r'.*[a-zA-Z]+') 
    # return bool(ko.fullmatch(text))
    return bool(en.match(text))  



# excel idx 
def _excel_index_creator(colum, row_idx):
    colum_idx = colum + str(row_idx)
    return colum_idx
    


# 한국어, 한자, 영어 추출
def _extract_db(raw_sent):
    ko, kot, en = '', '', ''
    ko_pattern = re.compile(r'[가-힇ㄱ-ㅎㅏ-ㅣ]')
    kot_pattern = re.compile(r'[一-龥]')
    en_pattern = re.compile(r'[a-zA-Z]')

    ko = re.findall(ko_pattern, raw_sent)
    kot = re.findall(kot_pattern, raw_sent)
    en = re.findall(en_pattern, raw_sent)
    
    print(ko, kot, en)
    return ko, kot, en

xlsx_file = './한국하천지명사전_1월_7일.xlsx'


# parsed to excel
def sent_to_excel(file_name):
    timestamp = datetime.now().strftime('%m%d%H%M')
    start = timeit.default_timer()
    
    # pdf에서 파싱된 raw 작업하기
    df = pd.read_excel(xlsx_file)   
    raw_data = df['raw'].tolist()
    
    #############################
    # excel 생성
    workbook = xlsxwriter.Workbook('./' + xlsx_file[:-4]  + '_pdf_'  + timestamp +'.xlsx') 
    worksheet = workbook.add_worksheet()

    # 셀 색칠하기
    cell_yellow = workbook.add_format()
    cell_yellow.set_pattern(1)
    cell_yellow.set_bg_color('yellow')

    worksheet.write('A1', '한국어', cell_yellow)
    worksheet.write('B1', '한자', cell_yellow)
    worksheet.write('C1', '영어', cell_yellow)
    row_idx = 2


    for raw_sent in raw_data:
        ko, kot, en = _extract_db(raw_sent)

        # A. Path 쓰기 (한국어)
        a_idx = _excel_index_creator('A', row_idx)
        worksheet.write(a_idx, ko)

        # B. Path 쓰기 (한자)
        b_idx = _excel_index_creator('B', row_idx)
        worksheet.write(b_idx, kot)

        # C. Path 쓰기 (영어)
        c_idx = _excel_index_creator('C', row_idx)
        worksheet.write(c_idx, en)
        
        
        print(row_idx)
        row_idx += 1

    workbook.close()
    stop = timeit.default_timer()

    print('PDF =====> Raw text to excel DONE (Running Time: ', stop - start, "sec.)")

sent_to_excel(xlsx_file)