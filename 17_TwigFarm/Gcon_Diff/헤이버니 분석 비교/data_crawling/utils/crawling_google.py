import time
import random
import xlsxwriter
from datetime import datetime

from bs4 import BeautifulSoup
from selenium import webdriver

from utils.common_functions import _excel_index_creator


# 구글 크롤링
def google_find_korean(ko_sent_df):
    en_google_sent_df = list()
    total_len = len(ko_sent_df)
    # 2. 웹브라우저 열기
    driver = webdriver.Chrome('/Users/haley/Downloads/chromedriver')
    url = 'https://translate.google.com/?hl=en&tab=TT&sl=ko&tl=en&op=translate'
    try:
        for idx, ko_sent in enumerate(ko_sent_df):
            sleep_time = random.randrange(3,5)
            driver.get(url)
            driver.find_element_by_css_selector('#yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.AxqVh > div.OPPzxe > c-wiz.rm1UF.UnxENd > span > span > div > textarea').click
            element_ko = driver.find_element_by_css_selector('c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.AxqVh > div.OPPzxe > c-wiz.rm1UF.UnxENd > span > span > div > textarea')
            element_ko.send_keys(ko_sent) # 한국어 보내기
            time.sleep(sleep_time) ## 5초
            element_en = driver.find_element_by_css_selector('c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.AxqVh > div.OPPzxe > c-wiz.P6w8m.BDJ8fb > div.dePhmb > div > div.J0lOec > span.VIiyi > span > span')# 
            en_sent = element_en.text
            en_google_sent_df.append(en_sent)
            print(f'{idx + 1}/{total_len} - {en_sent}')

    except:
        print(idx+1)
    
    return en_google_sent_df

# 구글 엑셀 쓰기
def _write_google_excel(range_idx, en_google_sent_df):
    timestamp = datetime.now().strftime('%m%d%H%M') 

    workbook = xlsxwriter.Workbook('./results/'  + '구글_' + str(range_idx) + '_' + timestamp + '_엑셀.xlsx')

    worksheet = workbook.add_worksheet()

    cell_yellow = workbook.add_format()
    cell_yellow.set_pattern(1)
    cell_yellow.set_bg_color(('yellow'))

    worksheet.write('A1', 'No')
    worksheet.write('B1', '구글', cell_yellow)

    row_idx = 2
    # 본격적으로 엑셀 쓰기
    for idx in range(len(en_google_sent_df)):
        a_idx = _excel_index_creator('A', row_idx)
        b_idx = _excel_index_creator('B', row_idx)

        worksheet.write(a_idx, str(row_idx - 1)) # 인덱스
        worksheet.write(b_idx, str(en_google_sent_df[idx])) # 원문

        row_idx += 1
    print(f'row_idx : {row_idx}')
    print('done')
    workbook.close()



