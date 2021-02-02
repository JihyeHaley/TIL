'''
    docx_mix_parser (병합)
    Word -> HTML raw text -> Excel 으로 변환
    문장 단위 1차 정제 후 엑셀 파일 생성
'''

import timeit
import xlsxwriter
from itertools import zip_longest
from datetime import datetime

import mammoth

def excel_index_creator(colum, row_idx):
    colum_idx = colum + str(row_idx)
    return colum_idx


stop_word = []

# mammoth 사용하여 docx raw test parsing
def docx_to_raw_text(file_name):
    with open(file_name, "rb") as docx_file:
        result = mammoth.extract_raw_text(docx_file)
        text = result.value  # The raw text
        messages = result.messages  # Any messages

    contents = text.split("\n")

    contents_prep = []
    for line in contents:
        if '。' in line:
            each_line = line.split('。')
            for each_each_line in each_line:
                if each_each_line in ['', ' ']:
                    continue
                else:
                    contents_prep.append(each_each_line+'。')
        elif '**' in line or '>>' in line or '--' in line:
            continue
        else:
            each_line = line.strip()
            contents_prep.append(each_line)
    print(contents_prep)
    return contents_prep

f_1 = '1. InnoRules Install Guide of Rule Builder.docx'
f_2 = '2. InnoRules User\'s Guide of Rule Builder(JP).docx'
f_3 = '3. InnoRules Installation and Operation Guide v7.2(JP).docx'
f_4 = '4. InnoRules Application Programming Interface Guide(JP).docx'
f_6 = '6. InnoProduct Repository Specification.docx'
f_7 = '7. InnoProduct Rule Service Guide of Product Builder.docx'
f_8 = '8. InnoProduct User\'s Guide of Product Builder-JP-20200323.docx'
f_9 = '9. InnoProduct Installation and Operation Guide of Product Builder.docx'


# 하나씩
def find_which_file():
    which_file = str(input())
    path = './jap/'
    file_name = ''
    if which_file == 'f_1':
        file_name = path + f_1
    elif which_file == 'f_2':
        file_name = path + f_2
    elif which_file == 'f_3':
        file_name = path + f_3
    elif which_file == 'f_4':
        file_name = path + f_4
    elif which_file == 'f_6':
        file_name = path + f_6
    elif which_file == 'f_7':
        file_name = path + f_7
    elif which_file == 'f_8':
        file_name = path + f_8
    elif which_file == 'f_9':
        file_name = path + f_9

    return file_name
    
# file_name = find_which_file()


# 파일에 path 
def file_name_with_path():
    file_lists = list()
    path = './jap/'
    file_lists.append(path + f_1)
    file_lists.append(path + f_2)
    file_lists.append(path + f_3)
    file_lists.append(path + f_4)
    file_lists.append(path + f_6)
    file_lists.append(path + f_7)
    file_lists.append(path + f_8)
    file_lists.append(path + f_9)

    return file_lists



def parsing_docx_at_once():

    start = timeit.default_timer()

    file_lists = file_name_with_path()
    total_row_cnt = 0
    completed_log = open(f'./docx_file' + '.txt', "w+")
    for idx, file_name in enumerate(file_lists):
        raw_data = docx_to_raw_text(file_name)
        # print(raw_data)
        print('#'*30)
        print(f'{idx+1}. file_name: {file_name}')
        print(f'raw data: {len(raw_data)}줄')
        workbook = xlsxwriter.Workbook('./parsed/' + file_name[6:]+'_.xlsx') 
        print('it works')
        worksheet = workbook.add_worksheet()

        row_idx = 1
        for raw_sent in raw_data:
            idx = excel_index_creator('A', row_idx)

            if raw_sent == '':
                continue
            else:
                input_raw_sent = raw_sent
            worksheet.write(idx, input_raw_sent)
            row_idx += 1
            
        print(f'excel idx: {row_idx}줄')
        total_row_cnt += row_idx
        completed_log.write(f'######################\n{file_name}\n엑셀:{row_idx}/\t{len(raw_data)}\n')
        workbook.close()

    stop = timeit.default_timer()    
    completed_log.close()
    print(f' DOCX_=====> Raw text to excel DONE (Running Time: {stop - start}sec.)')
    print(f'total_cnt: {total_row_cnt}')

parsing_docx_at_once()
# find_which_file()