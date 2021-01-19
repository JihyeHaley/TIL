'''
    main parser function
    --root_path: 렉스코드 클라우드 홈
    --sub_path: 분야별 폴더
'''

import argparse
from pathlib import Path


from parsers import xlsx_parser, pptx_parser
from parsers.docx_mix_parser import *
from parsers.docx_separate_parser import *

from utils.regex_functions import *
from utils.common_functions import *

TM_ROOT = str(Path.home()) + '/Lexcode/AI 학습용 한영 말뭉치 구축 채널 - 인공지능 학습 DB 구축 채널 - 인공지능 학습 DB 구축 채널/1. 원본DB(렉스코드)/'
DOC_ROOT = str(Path.home()) + '/Lexcode/AI 학습용 한영 말뭉치 구축 채널 - 인공지능 학습 DB 구축 채널 - 인공지능 학습 DB 구축 채널/3.학술정보/'


# parameter variables
parser = argparse.ArgumentParser(description='Parsing .docx files to HTML raw text, then convert to excel file.')

parser.add_argument('-sub', '--sub_path',
                    type=str, required=True,
                    help='<type: str> sub-directory for each category document files')

parser.add_argument('-type', '--dir_type',
                    type=str,
                    default = str(Path.home()) + '',
                    help='<type: str> TM or Academic Document')


args = parser.parse_args()

sub_path = args.sub_path
dir_type = args.dir_type


#  작업할 모든 파일 불러오기
def read_directory(dir_type, sub_path):

    if dir_type == 'TM':
        root_dir = TM_ROOT
    else:
        root_dir = DOC_ROOT

    # read and categorize file type
    xlsx_file_list = get_filename_list(root_dir, sub_path, '.xlsx')
    xls_file_list = get_filename_list(root_dir, sub_path, '.xls')
    xlsx_files = xlsx_file_list + xls_file_list

    pptx_files_list = get_filename_list(root_dir, sub_path, '.pptx')
    docx_files_list = get_filename_list(root_dir, sub_path, '.docx')

    # return excel, pptx, docx file list
    return (xlsx_files, pptx_files_list, docx_files_list)




# RUN Parser 
# 0:xlsx, 1:pptx, 2:docx
all_file_lists = read_directory(dir_type, sub_path)


# pass each file type
xlsx_parser.xlsx_to_excel(all_file_lists[0])
pptx_parser.pptx_to_excel(all_file_lists[1])


# if __name__ == '__main__':
#     html_raw_to_excel(root_path, sub_path)

