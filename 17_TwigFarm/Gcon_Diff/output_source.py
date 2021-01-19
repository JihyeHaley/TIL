import re
import timeit
import xlsxwriter
import pandas as pd

from datetime import datetime

from utils.common_funtions import _excel_index_creator
from input_source import _import_xlsx_to_list
from check_whtz_different import _wrtie_different_component


timestamp = datetime.now().strftime('%m%d%H%M') # time stamp

'''
    A           B          C
    Case_No     Input      Output
'''

# excel 쓰기
def create_excel_file():
    
    file_name, case_list = _import_xlsx_to_list()

    output_result_list, output_mor_list = _wrtie_different_component(case_list)

    # create xlsx
    workbook = xlsxwriter.Workbook('./' +  file_name + '_result_' + timestamp + '.xlsx')
    worksheet = workbook.add_worksheet()


    # cell color
    cell_yellow = workbook.add_format()
    cell_yellow.set_pattern(1)
    cell_yellow.set_bg_color(('yellow'))

    # write colum name
    worksheet.write('A1', 'Case_No', cell_yellow)
    worksheet.write('B1', 'Input', cell_yellow)
    worksheet.write('C1', 'Output', cell_yellow)
    worksheet.write('D1', 'Mor', cell_yellow)

    row_idx = 2

    for idx in range(len(case_list)):
        input_list = case_list[idx]
        output_list = output_result_list[idx]
        mor_list = output_mor_list[idx]

        a_idx = _excel_index_creator('A', row_idx) # no
        worksheet.write(a_idx, str(idx + 1))

        for jdx in range(len(input_list)):
            b_idx = _excel_index_creator('B', row_idx) # input
            c_idx = _excel_index_creator('C', row_idx) # output
            d_idx = _excel_index_creator('D', row_idx) # output
            
            worksheet.write(b_idx, input_list[jdx])
            worksheet.write(c_idx, output_list[jdx])
            worksheet.write(d_idx, str(mor_list[jdx]))
            row_idx += 1 

    workbook.close()

create_excel_file()