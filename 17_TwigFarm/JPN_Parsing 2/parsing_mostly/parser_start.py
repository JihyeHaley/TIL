"""
    main parser function
    --sub_path: 분야별 폴더
    --dir_type: 문서 타입별 root directory. - TM(용어집)/AD(학술정보원문파일)/직접절대경로입력
"""

import argparse
from pathlib import Path

from parsers import xlsx_parser, pptx_parser, docx_parser

from utils.regex_functions import *
from utils.common_functions import *

TM_ROOT = str(Path.home()) + "/Users/jihyeoh/Desktop/Desktop - Jeewon의 iMac/git/til/17_TwigFarm/JPN_Parsing 2"
DOC_ROOT = str(Path.home()) + "/Users/haley/Desktop/git/til/17_TwigFarm/JPN_Parsing 2/data"


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
    help="<type: str> TM(default) or AD or type root_path manually. /",
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
    xlsx_files_list = xlsx_file_list + xls_file_list

    pptx_files_list = get_filename_list(root_dir, sub_path, ".pptx")
    docx_files_list = get_filename_list(root_dir, sub_path, ".docx")
    pdf_file_list = get_filename_list(root_dir, sub_path, ".pdf")

    # return excel, pptx, docx file list
    return (xlsx_files_list, pptx_files_list, docx_files_list, pdf_file_list)
    # return pptx_files_list


# RUN Parser
# 0:xlsx, 1:pptx, 2:docx
all_file_lists = read_directory(root_type, sub_path)

# pass each file type
xlsx_parser.xlsx_to_excel(all_file_lists[0], sub_path)
pptx_parser.pptx_to_excel(all_file_lists[1], sub_path)
docx_parser.docx_parser_(all_file_lists[2], sub_path)
# pdf_parser.pdf_text_to_excel(all_file_lists[3], sub_path)