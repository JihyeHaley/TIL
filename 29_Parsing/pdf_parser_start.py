import argparse
from re import sub

from pdf_parsing import pdf_text_to_excel
from common_functions import *

# parameter variables
parser = argparse.ArgumentParser(
    description="PDF parser. Please use ABSOLUTE path as -r argument."
)

parser.add_argument(
    "-r",
    "--root_path",
    type=str,
    default= str(Path.home()) + "/Haley/",
    help="<type: str> root directory for each category document files (Default path = $HOME/)"
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

# 
# pdf_file_list = get_filename_list(root_path, ".pdf")
# pdf_file_list = ['./data/ESG_2.pdf']
# sub_path = 'data'
pdf_text_to_excel('./data/ESG_2.pdf', sub_path)


#
# def start(root_path, sub_path):
#     pdf_file_list = get_filename_list(root_path, sub_path, ".pdf")
#
#     pdf_text_to_excel(pdf_file_list, sub_path)
#
#
# if __name__ == '__main__':
#    start(root_path, sub_path)
