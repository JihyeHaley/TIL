"""
    main parser function
    --sub_path: 분야별 폴더
    --dir_type: 문서 타입별 root directory. - TM(용어집)/AD(학술정보원문파일)/직접절대경로입력
"""

import argparse
from pathlib import Path

from parsers import xlsx_parser, pptx_parser, docx_mix_parser, docx_separate_parser, pdf_parser

from utils.regex_functions import *
from utils.common_functions import *

TM_ROOT = str(Path.home()) + "/Lexcode/AI 학습용 한영 말뭉치 구축 채널 - 인공지능 학습 DB 구축 채널 - 인공지능 학습 DB 구축 채널/1. 원본DB(렉스코드)/"
DOC_ROOT = str(Path.home()) + "/Lexcode/AI 학습용 한영 말뭉치 구축 채널 - 인공지능 학습 DB 구축 채널 - 인공지능 학습 DB 구축 채널/3.학술정보/"


# parameter variables
parser = argparse.ArgumentParser(
    description="Parsing .docx files to HTML raw text, then convert to excel file."
)

parser.add_argument(
    "-s",
    "--sub_path",
    type=str,
    required=True,
    help="<type: str> sub-directory for each category document files",
)

parser.add_argument(
    "-r",
    "--root_type",
    type=str,
    default="TM",
    help="<type: str> TM(default) or AD or type root_path manually. ex)/Users/twigfarm/LexcodeDrive/학술정보/",
)

args = parser.parse_args()

sub_path = args.sub_path
root_type = args.root_type

#  작업할 모든 파일 불러오기
def read_directory(root_type, sub_path):

    if root_type == "TM":
        root_dir = TM_ROOT
    elif root_type == "AD":
        root_dir = DOC_ROOT
    else:
        root_dir = root_type

    # read and categorize file type
    xlsx_file_list = get_filename_list(root_dir, sub_path, ".xlsx")
    xls_file_list = get_filename_list(root_dir, sub_path, ".xls")
    xlsx_files = xlsx_file_list + xls_file_list

    pptx_files_list = get_filename_list(root_dir, sub_path, ".pptx")
    docx_files_list = get_filename_list(root_dir, sub_path, ".docx")
    # pdf_file_list = get_filename_list(root_dir, sub_path, ".pdf")

    # return excel, pptx, docx file list
    return (xlsx_files, pptx_files_list, docx_files_list)
    # return pptx_files_list


# RUN Parser
# 0:xlsx, 1:pptx, 2:docx
all_file_lists = read_directory(root_type, sub_path)

# pass each file type
xlsx_parser.xlsx_to_excel(all_file_lists[0], sub_path)
pptx_parser.pptx_to_excel(all_file_lists[1], sub_path)
docx_ko_files, docx_en_files, docx_mix_files, docx_non_lists = get_tm_doc_type(
    all_file_lists[2]
)
docx_separate_parser.docx_separate_to_excel(docx_ko_files, sub_path)
docx_mix_parser.docx_mix_to_excel(docx_mix_files, sub_path)
# pdf_parser.pdf_text_to_excel(all_file_lists[3], sub_path)


#if __name__ == '__main__':
#    html_raw_to_excel(root_path, sub_path)