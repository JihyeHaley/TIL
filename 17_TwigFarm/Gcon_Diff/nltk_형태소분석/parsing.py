import timeit
import xlsxwriter

from datetime import datetime

from utils import excel_index_creator, in_docx_to_raw_text

# timestamp = datetime.now().strftime('%m%d%H%M') 
file_name = 'nltk_형태소'

a = 'Our headquarters is in Seoul, but our R&D center is in Busan.'
b = 'Our headquarters is in Seoul, but the research and development center is in Busan.'

c = 'Our overseas office is in Chicago.'
d = 'Our company\'s overseas branch is located in Chicago.'

e = 'As soon as I hear from the customer, my secretary will turn the agenda.'
f = 'As soon as I hear from the client, my secretary will change the agenda.'

g = 'Stop by the new store on Brown Street!'
h = 'Please stop by the new store on Brown Street!'

i = 'From Monday, my new email address is mmin@gmail.com.'
j = 'Starting Monday, my new email address is mmin@gmail.com.'

k = 'I received the document by fax yesterday.'
l = 'I received the document by fax yesterday.'

a_splited = a.split(' ')
b_splited = b.split(' ')
stop_begin_idx = int()
stop_end_idx = int()

for idx in range(len(a_splited)):
    if a_splited[idx] == b_splited[idx]:
        continue
    else:
        stop_begin_idx = idx

for jdx in range(len(a_splited)):
    if a_splited[-jdx] == b_splited[-jdx]:
        continue
    else:
        stop_end_idx = jdx

print(a_splited[stop_begin_idx:stop_end_idx])
print(b_splited[stop_begin_idx:stop_end_idx])