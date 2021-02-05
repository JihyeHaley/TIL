import timeit
import xlsxwriter
import pandas as pd 

from datetime import datetime

from utils.common_functions import _excel_index_creator
from utils.import_excel import import_ko_df
from utils.crawling_google import google_find_korean

timestamp = datetime.now().strftime('%m%d%H%M') 

file_name = './data/4000_rest.xlsx'

ko_sent_df = import_ko_df(file_name)

google_find_korean(ko_sent_df)

