from tika import parser
from nltk import sent_tokenize
# from utils.regex_functions import quotes_cleaner
import os
import glob
import subprocess
import xlsxwriter


def get_filename_list(path, ext):
    print('Change encoding files.......\ \n')
    result = []
    for f in glob.glob(file_path + f"/*{ext}"):
        # run convmv shell script -> file normalization NFC -> NFD (한글자소분리해결)
        subprocess.run(['/usr/local/bin/convmv', '-f', 'utf-8', '-t', 'utf-8', '--nfc', '--notest', f])
        result.append(f)
    return result

root_path = '/Users/jihyeoh/주식회사 트위그팜/NIA - 예체능/'
sub_dir = '대한무용학회/2017'

file_path = root_path + sub_dir
pdf_file_lists = get_filename_list(file_path, '.pdf')


# def read_pdf_PDFMINER(pdf_file_lists):
#     i = 0
#     for pdf_file_list in pdf_file_lists:
#         parsed = parser.from_file(pdf_file_list)
#         print(parsed['content'].splitlines)



# read_pdf_PDFMINER(pdf_file_lists)
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
print(len(pdf_file_lists))

def read_pdf(pdf_file_lists):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    try:
        i = 0
        completed_log = open(f'./pdf_jihye/pdf_jihye' + '.txt', 'w+')
        for pdf_file_list in pdf_file_lists:
            i += 1
            device = TextConverter(rsrcmgr, retstr, laparams=laparams)
            read_pdf = open(pdf_file_list, 'rb')
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            password = ''
            maxpages = 0
            caching = True
            pagenos=set()
            pdf_text = ''

            for page in PDFPage.get_pages(read_pdf, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
                interpreter.process_page(page)
                pdf_text = retstr.getvalue()
                pdf_text = sent_tokenize(pdf_text)
            
            workbook = xlsxwriter.Workbook('./pdf_jihye/pdf_jihye' + str(i) + '_' + '.pdf' + '.xlsx')
            worksheet = workbook.add_worksheet()
            row_idx = 0
            for line in pdf_text:
                row_idx += 1
                worksheet.write('B' + str(row_idx), line)
                
            workbook.close()
            

            read_pdf.close()
            device.close()
            retstr.close()
            print('----------------------------------------------------------------')
            print(i, '-', pdf_text)
            completed_log.write(pdf_text + '\n')
    except Exception as e:
        print(str(e))


read_pdf(pdf_file_lists)