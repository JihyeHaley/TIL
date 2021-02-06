import time
import random
import xlsxwriter
from datetime import datetime

from bs4 import BeautifulSoup
from selenium import webdriver

from utils.common_functions import _excel_index_creator


# 구글 크롤링
def kakao_find_korean(ko_sent_df):
    en_kakao_sent_df = list()
    total_len = len(ko_sent_df)
    # 2. 웹브라우저 열기
    driver = webdriver.Chrome('/Users/haley/Downloads/chromedriver')
    url = 'https://translate.kakao.com/'

    timestamp = datetime.now().strftime('%m%d%H%M') 

    workbook = xlsxwriter.Workbook('./results/kakao/'  + '카카오_' + timestamp + '_엑셀.xlsx')

    worksheet = workbook.add_worksheet()

    cell_yellow = workbook.add_format()
    cell_yellow.set_pattern(1)
    cell_yellow.set_bg_color(('yellow'))

    worksheet.write('A1', 'No')
    worksheet.write('B1', '원문', cell_yellow)
    worksheet.write('C1', '카카오', cell_yellow)

    row_idx = 2

    try:
        for idx, ko_sent in enumerate(ko_sent_df):
            sleep_time = random.randrange(3,5)
            driver.get(url)
            driver.find_element_by_css_selector('#query').click
            element_ko = driver.find_element_by_css_selector('#query')
            element_ko.send_keys(ko_sent) # 한국어 보내기
            time.sleep(sleep_time) ## 5초
            element_en = driver.find_element_by_css_selector('#result')# 
            en_sent = element_en.text
            en_kakao_sent_df.append(en_sent)
            print(f'{idx + 1}/{total_len} - {en_sent}')
            a_idx = _excel_index_creator('A', row_idx)
            b_idx = _excel_index_creator('B', row_idx)
            c_idx = _excel_index_creator('C', row_idx)

            worksheet.write(a_idx, str(row_idx - 1)) # 인덱스
            worksheet.write(b_idx, str(ko_sent)) # 원문
            worksheet.write(c_idx, str(en_sent)) # 카카오
            row_idx += 1
        workbook.close()

    except:
        print('error')
    
    return en_kakao_sent_df
