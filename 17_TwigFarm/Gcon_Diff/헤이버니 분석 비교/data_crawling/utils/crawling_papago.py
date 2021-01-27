import pandas as pd

import time

from bs4 import BeautifulSoup
from selenium import webdriver


def papago_find_korean(ko_sent_df):
    en_papago_sent_df = list()
    total_len = len(ko_sent_df)

    # 2. 웹브라우저 열기
    driver = webdriver.Chrome('/Users/haley/Downloads/chromedriver')
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%EB%B2%88%EC%97%AD'
    
    for idx, ko_sent in enumerate(ko_sent_df):
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

    print(en_papago_sent_df)  
    return en_papago_sent_df