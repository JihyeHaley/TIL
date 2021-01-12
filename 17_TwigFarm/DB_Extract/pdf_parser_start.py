import argparse

from pdf_parser import _pdf_text_to_list
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
pdf_file_list = get_filename_list(root_path, sub_path, '.pdf')

# step 2. raw data filter
pdf_filtered_list, pdf_failed_list = _pdf_text_to_list(pdf_file_list)

# step 3. filtered data excel로 작성하기
word_extract_to_word(pdf_filtered_list, pdf_failed_list)