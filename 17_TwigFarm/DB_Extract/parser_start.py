import argparse

from parser_pdf import pdf_text_to_list
from parser_pptx import pptx_text_to_list
from parser_docx import docx_text_to_list
from parser_xlsx import xlsx_text_to_list

from utils.common_functions import get_filename_list
from extract_check_to_excel import word_extract_to_word

# parameter variables
parser = argparse.ArgumentParser(
    description='PDF parser. Please use ABSOLUTE path as -r argument.'
)

parser.add_argument(
    '-r',
    '--root_path',
    type=str,
    help='<type: str> root directory for each category document files (Default path = $HOME/Users/haley/Desktop/JPN_Parsing/)'
)

parser.add_argument(
    '-s',
    '--sub_path',
    type=str,
    required=True,
    help='<type: str> sub-directory for each category document files'
)


args = parser.parse_args()

root_path = args.root_path
sub_path = args.sub_path

# step 1. 파일 가져오기
pptx_file_list = get_filename_list(root_path, sub_path, '.pptx')
docx_file_list = get_filename_list(root_path, sub_path, '.docx')
xlsx_file_list = get_filename_list(root_path, sub_path, '.xlsx')
pdf_file_list = get_filename_list(root_path, sub_path, '.pdf')

# step 2. raw data filter
pptx_filtered_dict, pptx_failed_dict = pptx_text_to_list(pptx_file_list, sub_path)
docx_filtered_dict, docx_failed_dict = docx_text_to_list(docx_file_list, sub_path)
xlsx_filtered_dict, xlsx_failed_dict = xlsx_text_to_list(xlsx_file_list, sub_path)
pdf_filtered_dict, pdf_failed_dict = pdf_text_to_list(pdf_file_list, sub_path)

total_filtered_dict = {**pdf_filtered_dict, **pptx_filtered_dict, **docx_filtered_dict, **xlsx_filtered_dict}
total_failed_dict = {**pdf_failed_dict, **pptx_failed_dict, **docx_failed_dict, **xlsx_failed_dict}

for key, value in total_failed_dict.items():
    print(key,'-', len(value))

# step 3. filtered data excel로 작성하기
word_extract_to_word(total_filtered_dict, total_failed_dict, sub_path)