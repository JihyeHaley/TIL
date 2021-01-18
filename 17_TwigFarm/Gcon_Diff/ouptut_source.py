import re
import timeit
import xlsxwriter
import pandas as pd

from datetime import datetime

from utils.common_funtions import _excel_index_creator
from check_whtz_different import return_to_output_source


timestamp = datetime.now().strftime('%m%d%H%M') # time stamp
file_name, output_result_list = return_to_output_source()

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
row_idx = 2

'''
    A           B          C
    Case_No     Input      Output
'''

