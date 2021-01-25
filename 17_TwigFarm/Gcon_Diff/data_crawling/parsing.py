import timeit
import xlsxwriter

from datetime import datetime

from utils import excel_index_creator, in_docx_to_raw_text

# timestamp = datetime.now().strftime('%m%d%H%M') 
file_name = '1'


# 형태소와 의미를 쪼개기
def _split_sent(file_name):
    sentence_list = list()
    raw_contents = in_docx_to_raw_text(file_name)

    print(f'raw_contesnt : {len(raw_contents)}')
    
    cnt = 0
    for raw_content in raw_contents:
        if raw_content == '':
            continue
        chunk = raw_content.split(' ')
        chunk.pop(0)

        sentence_pre = str()
        for component in chunk:
            sentence_pre += component + ' '

        sentence_pre_list = sentence_pre.split(':')
        for sentence_pre in sentence_pre_list:
            sentence_list.append(sentence_pre)
        
        cnt += 1 
    print(f'cnt : {cnt}')
    return sentence_list


# 엑셀에 쓰기
def write_in_the_excel(file_name):
    sentence_list = _split_sent(file_name)
    workbook = xlsxwriter.Workbook('./' + file_name + '_엑셀.xlsx')

    worksheet = workbook.add_worksheet()

    cell_yellow = workbook.add_format()
    cell_yellow.set_pattern(1)
    cell_yellow.set_bg_color(('yellow'))

    worksheet.write('A1', 'No')
    worksheet.write('B1', '관형', cell_yellow)
    row_idx = 2
    for sentence in sentence_list:
        a_idx = excel_index_creator('A', row_idx)
        b_idx = excel_index_creator('B', row_idx)
        worksheet.write(a_idx, str(row_idx - 1)) # 인덱스
        worksheet.write(b_idx, str(sentence)) # 형태소 
        row_idx += 1
    print(f'row_idx : {row_idx}')
    print('done')
    workbook.close()

write_in_the_excel(file_name)