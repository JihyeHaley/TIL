import mammoth
import glob
import re
import os
import xlsxwriter
import timeit
from itertools import zip_longest

def is_skip(text):
    skip = re.compile('^[0-9『』@%#^&~!★●▪:;()/=+*$,._\\\\-\\s]+')
    return bool(skip.fullmatch(text))


def is_page_num(text):
    is_page = re.compile('.[0-9|pP[\\]{}()<>\\s]+')
    return bool(is_page.fullmatch(text))

skip_word = []

file_name_lists = [f for f in glob.glob(f'./4.2019한국표준협회/*.*x')]
file_name_lists_doc = [f for f in glob.glob(f'./4.2019한국표준협회/*.doc')]
docx_name_lists = []
pptx_name_lists = []

for file_name_list in file_name_lists:    
# print(file_name_list[-8:-5], ' ') # 한/영

    # docx 분류
    if file_name_list[-5:] == '.docx':
        docx_name_lists.append(file_name_list)

    # pptx 분류
    elif file_name_list[-5:] == '.pptx':
        pptx_name_lists.append(file_name_list)
    

# for file_name_list_doc in file_name_lists_doc:
#     docx_name_lists.append(file_name_list_doc)


# docx dict 만들기
file_lists_docx = {}
i = 0

for docx_name_list in docx_name_lists:
    i += 1
    docx_results = []
    print(docx_name_list[15:])
#       worksheet.write('A' + str(row_idx), ">" * 20 + docx_name_list)
    with open(docx_name_list, "rb") as docx_file:
        result = mammoth.extract_raw_text(docx_file)
        text = result.value  # The raw text
        contents = text.split('\n |" "')

    for line in contents:
        line.replace(".", ". ")
    docx_results = text.split('\n')
    print('done')
    
    file_lists_docx[docx_name_list[15:]] = docx_results

print(f'done, file_lists_docx : is {len(file_lists_docx)}')


    