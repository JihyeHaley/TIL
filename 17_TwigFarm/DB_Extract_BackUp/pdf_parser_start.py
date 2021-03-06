'''
    pdf parser starter
    --path : pdf file directory

    script example: python pdf_parser_start.py -s '사회과학' -r '/Users/twigfarm/Desktop/'

'''

import argparse

from pdf_parser import _pdf_text_to_list
from utils.common_functions import get_filename_list
from extract_check_to_excel import word_extract_to_word

#PDF_ROOT = str(Path.home()) + '/주식회사 트위그팜/NIA - 01_원문/'
#PDF_ROOT = str(Path.home()) + '/Desktop/'

# parameter variables
parser = argparse.ArgumentParser(
    description='PDF parser. Please use ABSOLUTE path as -r argument.'
)

parser.add_argument(
    '-r',
    '--root_path',
    type=str,
    # default= str(Path.home()) + '/Users/haley/Desktop/Git/TIL/17_Twigfarm/DB_EXTRACT/',
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


pdf_file_list = get_filename_list(root_path, sub_path, '.pdf')
pdf_filtered_list, pdf_failed_list = _pdf_text_to_list(pdf_file_list)
word_extract_to_word(pdf_filtered_list, pdf_failed_list)