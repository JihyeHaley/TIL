import time
import random
import xlsxwriter
import pandas as pd

from datetime import datetime

from bs4 import BeautifulSoup
from selenium import webdriver

from utils.common_functions import _excel_index_creator

# 파파고 크롤링
def papago_find_korean(ko_sent_df):
    en_papago_sent_df = list()
    total_len = len(ko_sent_df)
    # 2. 웹브라우저 열기
    driver = webdriver.Chrome('/Users/haley/Downloads/chromedriver')
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%EB%B2%88%EC%97%AD'
   
    try:
        for idx, ko_sent in enumerate(ko_sent_df):
            sleep_time = random.randrange(3,5)
            # 3. 입력하기
            driver.get(url)
            driver.find_element_by_css_selector('#_au_translator > div.tlans_box > div.txt_box._input > div.txt_area._view > textarea').click
            element_ko = driver.find_element_by_css_selector('#_au_translator > div.tlans_box > div.txt_box._input > div.txt_area._view > textarea')
            element_ko.send_keys(ko_sent) # 한국어 보내기
            time.sleep(5) ## 5초
            element_en = driver.find_element_by_css_selector('#_au_translator > div.tlans_box > div.txt_box.rt._output.on > div.txt_area._view > p') 
            en_sent = element_en.text
            en_papago_sent_df.append(en_sent)
            print(f'{idx + 1}/{total_len} - {en_sent}')
    except:
        print(idx+1)
    return en_papago_sent_df

# 파파고 엑셀 쓰기
def _write_papago_excel(range_idx, en_papago_sent_df):
    
    timestamp = datetime.now().strftime('%m%d%H%M') 

    workbook = xlsxwriter.Workbook('./results/'  + '파파고_' + str(range_idx) + '_' + timestamp + '_엑셀.xlsx')

    worksheet = workbook.add_worksheet()

    cell_yellow = workbook.add_format()
    cell_yellow.set_pattern(1)
    cell_yellow.set_bg_color(('yellow'))

    worksheet.write('A1', 'No')
    worksheet.write('B1', '파파고', cell_yellow)

    row_idx = 2
    # 본격적으로 엑셀 쓰기
    for idx in range(len(en_papago_sent_df)):
        a_idx = _excel_index_creator('A', row_idx)
        b_idx = _excel_index_creator('B', row_idx)

        worksheet.write(a_idx, str(row_idx - 1)) # 인덱스
        worksheet.write(b_idx, str(en_papago_sent_df[idx])) # 원문

        row_idx += 1
    print(f'row_idx : {row_idx}')
    print('done')
    workbook.close()
