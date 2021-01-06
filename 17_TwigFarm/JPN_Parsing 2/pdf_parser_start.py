"""
    pdf parser starter
    --path : pdf file directory

    script example: python pdf_parser_start.py -s "사회과학" -r "/Users/twigfarm/Desktop/"

"""

import argparse

from parsers.pdf_parser import pdf_text_to_excel
from utils.common_functions import *

#PDF_ROOT = str(Path.home()) + "/주식회사 트위그팜/NIA - 01_원문/"
#PDF_ROOT = str(Path.home()) + "/Desktop/"

# parameter variables
parser = argparse.ArgumentParser(
    description="PDF parser. Please use ABSOLUTE path as -r argument."
)

parser.add_argument(
    "-r",
    "--root_path",
    type=str,
    default= str(Path.home()) + "/Users/haley/Desktop/JPN_Parsing/",
    help="<type: str> root directory for each category document files (Default path = $HOME/Users/haley/Desktop/JPN_Parsing/)"
)

parser.add_argument(
    "-s",
    "--sub_path",
    type=str,
    required=True,
    help="<type: str> sub-directory for each category document files"
)


args = parser.parse_args()

root_path = args.root_path
sub_path = args.sub_path


pdf_file_list = get_filename_list(root_path, sub_path, ".pdf")
pdf_text_to_excel(pdf_file_list, sub_path)


#
# def start(root_path, sub_path):
#     pdf_file_list = get_filename_list(root_path, sub_path, ".pdf")
#
#     pdf_text_to_excel(pdf_file_list, sub_path)
#
#
# if __name__ == '__main__':
#    start(root_path, sub_path)
