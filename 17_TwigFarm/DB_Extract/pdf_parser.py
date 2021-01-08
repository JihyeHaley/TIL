'''
    pdf parser
'''

from datetime import datetime
import timeit
import xlsxwriter
from tqdm import tqdm
import re

from pdf_utils import _isContainKo, _isContainKoT, _isContainEn, _read_pdf_to_text
from word_pos_test import _start_mecab


## excel idx 
def _excel_index_creator(colum, row_idx):
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
            workbook = xlsxwriter.Workbook('./' + each_file[-12:-4]  + '_pdf_'  + timestamp +'.xlsx') 
            worksheet = workbook.add_worksheet()
            
            # 셀 색칠 
            cell_yellow = workbook.add_format()
            cell_yellow.set_pattern(1)
            cell_yellow.set_bg_color('yellow')
            worksheet.write('A1', 'no')
            worksheet.write('B1', 'Raw', cell_yellow)
            worksheet.write('C1', 'Mecab', cell_yellow)

            row_idx = 2

            # read pdf files and get as text list
            pdf_text_list = _read_pdf_to_text(each_file)
            print(len(pdf_text_list))

            # for line in pdf_text_list:
            #     each_line = line.strip()
                

            for sent in pdf_text_list:
                # 한국어, 한자, 영어 셋 중 하나라도 없으면 그냥 패스 
                if _isContainKo(sent) and _isContainKoT(sent) and _isContainEn(sent)== True:
                    output_sent = re.sub(r'▶', '',sent)
                    if _isContainKoT(output_sent) == True:
                        a_idx = _excel_index_creator('A', row_idx)
                        b_idx = _excel_index_creator('B', row_idx)
                        c_idx = _excel_index_creator('C', row_idx)
                        
                        # a. no 쓰기
                        worksheet.write(a_idx, str(row_idx - 1))

                        # b. raw 쓰기
                        output_sent = re.sub(r'▶', '',sent)
                        worksheet.write(b_idx, output_sent)
                        
                        # c. mecab 쓰기
                        te = _start_mecab(output_sent)
                        worksheet.write(c_idx, str(te))

                        print(row_idx)
                        row_idx += 1
         
            workbook.close()
        stop = timeit.default_timer()

        print('PDF =====> Raw text to excel DONE (Running Time: ', stop - start, "sec.)")
