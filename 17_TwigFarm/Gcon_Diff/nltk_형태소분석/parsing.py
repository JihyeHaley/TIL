import timeit
import xlsxwriter

from datetime import datetime

from utils import excel_index_creator, in_docx_to_raw_text

# timestamp = datetime.now().strftime('%m%d%H%M') 
file_name = 'nltk_형태소'


# 형태소와 의미를 쪼개기
def _split_mor_mean(file_name):
    mor_mean_dict = dict()
    raw_contents = in_docx_to_raw_text(file_name)
    print(f'raw_contesnt : {len(raw_contents)}')
    cnt = 0
    for raw_content in raw_contents:
        chunk = raw_content.split(' ')
        dict_key = chunk[0]
        dict_value = raw_content[len(dict_key):]
        mor_mean_dict[dict_key] = dict_value
        cnt += 1 
    print(f'cnt : {cnt}')
    return mor_mean_dict


# 엑셀에 쓰기
def write_in_the_excel(file_name):
    mor_mean_dict = _split_mor_mean(file_name)
    workbook = xlsxwriter.Workbook('./' + file_name + '_엑셀.xlsx')

    worksheet = workbook.add_worksheet()

    cell_yellow = workbook.add_format()
    cell_yellow.set_pattern(1)
    cell_yellow.set_bg_color(('yellow'))

    worksheet.write('A1', 'No')
    worksheet.write('B1', 'Mor(형태소)', cell_yellow)
    worksheet.write('C1', 'Meaning(의미)', cell_yellow)
    row_idx = 2
    empty_cnt = 0
    for key, value in mor_mean_dict.items():
        a_idx = excel_index_creator('A', row_idx)
        b_idx = excel_index_creator('B', row_idx)
        c_idx = excel_index_creator('C', row_idx)
        if (key and value) == '':
            empty_cnt += 1
            continue
        worksheet.write(a_idx, str(row_idx - 1)) # 인덱스
        worksheet.write(b_idx, str(key)) # 형태소 
        worksheet.write(c_idx, str(value)) # 의미
        row_idx += 1
    print(f'empty_cnt : {empty_cnt}')
    print(f'row_idx : {row_idx}')
    print('done')
    workbook.close()

write_in_the_excel(file_name)