import time
import random
import xlsxwriter
from datetime import datetime

from bs4 import BeautifulSoup
from selenium import webdriver

from common_functions import _excel_index_creator

# 2. 웹브라우저 열기
def google():
    google_driver = webdriver.Chrome('/Users/haley/Downloads/chromedriver')
    google_url = 'https://translate.google.com/?hl=en&tab=TT&sl=ko&tl=en&op=translate'
    google_driver.get(google_url)
    return google_driver, google_url


# 2. 웹브라우저 열기
def papago():
    papago_driver = webdriver.Chrome('/Users/haley/Downloads/chromedriver')
    papago_url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%EB%B2%88%EC%97%AD'
    papago_driver.get(papago_url)
    return papago_driver, papago_url


# 구글 크롤링
def google_find_korean(driver, url, ko_sent):
    
    sleep_time = random.randrange(3,5)
    driver.get(url)
    driver.find_element_by_css_selector('#yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.AxqVh > div.OPPzxe > c-wiz.rm1UF.UnxENd > span > span > div > textarea').click
    element_ko = driver.find_element_by_css_selector('c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.AxqVh > div.OPPzxe > c-wiz.rm1UF.UnxENd > span > span > div > textarea')
    element_ko.send_keys(ko_sent) # 한국어 보내기
    time.sleep(sleep_time) ## 5초
    element_en = driver.find_element_by_css_selector('c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.AxqVh > div.OPPzxe > c-wiz.P6w8m.BDJ8fb > div.dePhmb > div > div.J0lOec > span.VIiyi > span > span')# 
    google_en_sent = element_en.text

    
    return google_en_sent

# 파파고 크롤링
def papago_find_korean(driver, url, ko_sent):
    
    sleep_time = random.randrange(3,5)
    # 3. 입력하기
    driver.get(url)
    driver.find_element_by_css_selector('#_au_translator > div.tlans_box > div.txt_box._input > div.txt_area._view > textarea').click
    element_ko = driver.find_element_by_css_selector('#_au_translator > div.tlans_box > div.txt_box._input > div.txt_area._view > textarea')
    element_ko.send_keys(ko_sent) # 한국어 보내기
    time.sleep(sleep_time) ## 5초
    element_en = driver.find_element_by_css_selector('#_au_translator > div.tlans_box > div.txt_box.rt._output.on > div.txt_area._view > p') 
    papago_en_sent = element_en.text

    return papago_en_sent






