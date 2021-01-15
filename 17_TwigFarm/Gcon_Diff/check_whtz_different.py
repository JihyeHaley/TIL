import re
import timeit

from datetime import datetime
from input_source import xlsx_to_list

# import and save as list
file_name, case_list = xlsx_to_list()
output_result_list = list()


# find what is different components in the sentence
def _check_whtz_different(case_list):
    for case_sent in case_list:
        

    return output_result_list


def return_to_output_source():
    return file_name, output_result_list