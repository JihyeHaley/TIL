'''
    Write excel file for the corpus data tracking
'''


from pathlib import Path
from unicodedata import normalize
import xlsxwriter
from PyPDF2 import PdfFileReader

root_path = '/주식회사 트위그팜/NIA - 01_원문/'

def arrange_files(ext, root_path):
    files_list = []
    for f in Path(str(Path.home()) + root_path + '사회과학/').rglob(f'*{ext}'):
        files_list.append(str(f.parent)+'/'+f.name)

    files_list = [ normalize("NFC", f) for f in files_list ]

    # 결과 엑셀파일 정의.
    workbook = xlsxwriter.Workbook(ext[1:] + '_data.xlsx')
    worksheet = workbook.add_worksheet()
    cell_format = workbook.add_format({'align': 'center', 'valign': 'vcenter', 'border': 1})
    title_format = workbook.add_format({'align': 'center', 'valign': 'vcenter', 'border': 1 , 'fg_color': 'yellow'})

    worksheet.write('A1', '순번' ,title_format)
    worksheet.write('B1', '분야' , title_format)
    worksheet.write('C1', '데이터출처',title_format)
    worksheet.write('D1', '연도' , title_format)
    worksheet.write('E1', '파일명' ,title_format)
    worksheet.write('F1', '페이지수', title_format)
    row_idx = 2

    # cell merge를 위한 체크 리스트.
    check_file_field = []
    check_file_source = []
    check_file_year = []

    for each_file in files_list:

        print(each_file + '작업을 시작합니다.')

        pdf_file = PdfFileReader(open(each_file, 'rb'))
        num_pages = pdf_file.getNumPages()

        splited_each_file_list = each_file.split(root_path)[-1].split('/')
        if len(splited_each_file_list) == 3:
            file_field = splited_each_file_list[0]
            file_source = splited_each_file_list[1]
            file_year = '-'
            file_name = splited_each_file_list[2]
        elif len(splited_each_file_list) == 4:
            file_field = splited_each_file_list[0]
            file_source = splited_each_file_list[1]
            file_year = splited_each_file_list[2]
            file_name = splited_each_file_list[3]
        else:
            print('--- ERROR --- ')
            print(each_file + '경로에 문제가 있습니다.')
            continue
        
        
        
        worksheet.write("A" + str(row_idx), str(row_idx - 1), cell_format)
        worksheet.write("E" + str(row_idx), str(file_name), cell_format)
        worksheet.write("F" + str(row_idx), str(num_pages), cell_format)
    
        # cell 값이 같지 않을때 이전 값들을 merge를 진행.
        if check_file_field and check_file_field[-1] != file_field:
            worksheet.merge_range("B" + str(row_idx - len(check_file_field))+':'+"B"+str(row_idx -1), str(check_file_field[-1]), cell_format)
            check_file_field = []
        if check_file_source and check_file_source[-1] != file_source:
            worksheet.merge_range("C" + str(row_idx - len(check_file_source))+':'+"C"+str(row_idx -1), str(check_file_source[-1]), cell_format)
            check_file_source = []
        if check_file_year and check_file_year[-1] != file_year:
            worksheet.merge_range("D" + str(row_idx - len(check_file_year))+':'+"D"+str(row_idx -1), str(check_file_year[-1]), cell_format)
            check_file_year = []

        # merge를 위해 체크 리스트에 값들을 저장.
        check_file_field.append(file_field)
        check_file_source.append(file_source)
        check_file_year.append(file_year)

        row_idx += 1

    # 마지막으로 체크 리스트에 남아있는 값들을 merge 진행.
    worksheet.merge_range("B" + str(row_idx - len(check_file_field))+':'+"B"+str(row_idx -1), str(check_file_field[-1]), cell_format)
    worksheet.merge_range("C" + str(row_idx - len(check_file_source))+':'+"C"+str(row_idx -1), str(check_file_source[-1]), cell_format)
    worksheet.merge_range("D" + str(row_idx - len(check_file_year))+':'+"D"+str(row_idx -1), str(check_file_year[-1]), cell_format)
    workbook.close()


arrange_files('.pdf' , root_path)
