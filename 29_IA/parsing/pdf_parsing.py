'''
    pdf parser
'''

from datetime import datetime
import timeit
import xlsxwriter
from common_functions import *
from regex_functions import *
from read_pdf import *
from tqdm import tqdm


# Intro 제목
title_regex = re.compile(r'((^\d\.|[Ⅰ|II|Ⅱ|Ⅲ|Ⅳ|Ⅴ]\.)(\d\.){0,})\s{0,}([\D[ㄱ-ㅣ가-힣|a-zA-Z].*)')

# 일반 웹사이트 주소
web_regex = re.compile(r'((http)s{0,1}://)?[\s]{0,1}[-a-z0-9]{0,3}\.{0,1}[-a-z0-9@:%._\\+~#=]{2,256}\.[a-z]{2,4}', re.IGNORECASE)

# 이메일주소
email_regex = re.compile(r'([a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}.{0,1}\w{0,4})', re.IGNORECASE)

# 전화번호 - 021231234(5), (02(2)-123(3)-1234), (02)988-9873, 1234-1234
phone_regex = re.compile(r'[\[<{\(]{0,1}(([\[<{\(]{0,1}[\☎\☏]{0,1}[\s]{0,1}[0-9]{0,3}[}>\)\]]{0,1}\-{0,1}[0-9]{3,4}\-{0,1}[0-9]{3,4})|([0-9]{9,10}))[}>\)\]]{0,1}')

# 날짜 - yyyy.mm.dd | mm.dd.yyyy | dd.mm.yyyy
date_regex = re.compile(r'((\d{4})([\s./-]{0,3})(0[1-9]|1[012]|[1-9])([\s./-]{0,3})(0[1-9]|[12][0-9]|3[0-1]|[1-9])([\s./-]{0,3}))'\
            '|((0[1-9]|1[012]|[1-9])([\s./-]{0,3})(0[1-9]|[12][0-9]|3[0-1]|[1-9])([\s./-]{0,3})(\d{4})([\s./-]{0,3}))'\
            '|((0[1-9]|[12][0-9]|3[0-1]|[1-9])([\s./-]{0,3})(0[1-9]|1[012]|[1-9])([\s./-]{0,3})(\d{4})([\s./-]{0,3}))')


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

        error_cnt = 0
        # Open and create each excel file
        workbook = xlsxwriter.Workbook('./results/' +  sub_path  + '_pdf_'  + timestamp +'.xlsx') 
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'KOR')
      
        row_idx = 2
        total_cnt = 0

        # completed_log = open(f'./results/' + sub_path  + '/'  + sub_path + '_log_pptx_' + timestamp + '.txt', "w+")
        
        pdf_parsed = read_pdf_to_text(pdf_file_list)
        try:
            for line in pdf_parsed:
                a_idx =excel_index_creator('A', row_idx)
                worksheet.write(a_idx, line)
                total_cnt += 1
                row_idx += 1 
            

        # Write Error log file when docx -> txt
        except Exception as e:
            print('PDF_[ERROR]' + each_file + str(e) +' got ERROR!')
            # completed_log.write('[ERROR MESSAGE]' + each_file + str(e) + '\n')

        workbook.close()
        # completed_log.close()
        stop = timeit.default_timer()

        print('PDF =====> Raw text to excel DONE (Running Time: ', stop - start, "sec.)")
        print('Total CNT: ', total_cnt)
