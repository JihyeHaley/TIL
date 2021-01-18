import re
import timeit
import xlsxwriter
import pandas as pd

from datetime import datetime

# import xlsx and read input source then save to list
def xlsx_to_list():
    # file import 
    file_name = str(input())
    xlsx_file = f'./{file_name}.xlsx'

    # read data
    df = pd.read_excel(xlsx_file)
    case_list = df['input'].tolist()

    return file_name, case_list


