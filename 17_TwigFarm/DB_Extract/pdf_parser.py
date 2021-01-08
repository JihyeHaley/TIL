'''
    pdf parser
'''

from datetime import datetime
import timeit
import xlsxwriter
from tqdm import tqdm
from read_pdf import read_pdf_to_text
import re


# 일본어
# [あ-んァ-ソ]


# 한국어
def isContainKo(text):
    ko = re.compile(r'.*[가-힇ㄱ-ㅎㅏ-ㅣ]+') 
    # return bool(ko.fullmatch(text))
    return bool(ko.match(text))  


# 한자
def isContainKoT(text):
    kot = re.compile(r'.*[一-龥]+') 
    # return bool(ko.fullmatch(text))
    return bool(kot.match(text))   


# 영어
def isContainEn(text):
    en = re.compile(r'.*[a-zA-Z]+') 
    # return bool(ko.fullmatch(text))
    return bool(en.match(text))  



## excel idx 
def excel_index_creator(colum, row_idx):
    colum_idx = colum + str(row_idx)
    return colum_idx
    

def pdf_text_to_excel(pdf_file_list, sub_path):
    if len(pdf_file_list) == 0:
        print('''-----------------------------------------------------------
        PDF파일 없습니다.
        ''')
    else:
        print('''-----------------------------------------------------------
        PDF 작업 시작합니다.
        ''')
        # for time stamp
        timestamp = datetime.now().strftime('%m%d%H%M')
        start = timeit.default_timer()

        
        

        for each_file in tqdm(pdf_file_list):
            # Open and create each excel file
            workbook = xlsxwriter.Workbook('./' + each_file[-11:-4]  + '_pdf_'  + timestamp +'.xlsx') 
            worksheet = workbook.add_worksheet()
            
            # 셀 색칠 
            cell_yellow = workbook.add_format()
            cell_yellow.set_pattern(1)
            cell_yellow.set_bg_color('yellow')
            worksheet.write('A1', 'raw', cell_yellow)

            row_idx = 2

            # read pdf files and get as text list
            pdf_text_list = read_pdf_to_text(each_file)
            print(len(pdf_text_list))

            # for line in pdf_text_list:
            #     each_line = line.strip()
                

            for sent in pdf_text_list:

                # 한국어, 한자, 영어 셋 중 하나라도 없으면 그냥 패스 
                if isContainKo(sent) and isContainKoT(sent) and isContainEn(sent)== True:
                    # A. Path 쓰기
                    a_idx =excel_index_creator('A', row_idx)
                    worksheet.write(a_idx, sent)
                    print(row_idx)
                    row_idx += 1
         
            workbook.close()
        stop = timeit.default_timer()

        print('PDF =====> Raw text to excel DONE (Running Time: ', stop - start, "sec.)")
