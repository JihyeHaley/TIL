import re
import timeit
import xlsxwriter
import pandas as pd

from datetime import datetime

# import xlsx and read input source then save to list
def _import_xlsx_to_list():
    # file import 
    # file_name = str(input('파일 명을 적어주세요(확장자 xlsx default적지마세요): '))
    file_name = 'input'
    xlsx_file = f'./{file_name}.xlsx'

    # read data
    df = pd.read_excel(xlsx_file)
    file_input = df['input'].tolist()
    case_list = list()
    '''
    0, 1, 2, // 3, 4, 5, // 6, 7, 8,
    '''
    for idx in range(0, len(file_input), 3):
        group_list = list()
        for jdx in range(idx, idx+3):
            group_list.append(file_input[jdx])
        case_list.append(group_list)

    return file_name, case_list


