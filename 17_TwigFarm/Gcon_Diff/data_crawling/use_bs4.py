import pandas as pd

from bs4 import BeautifulSoup
from selenium import webdriver
import time

xlsxFile = './1_엑셀.xlsx'

df = pd.read_excel(xlsxFile)
ko_sent_df = df['관형'].tolist()
print(ko_sent_df)

def find_korean(ko_sent_df):
    # 2. 웹브라우저 열기
    driver = webdriver.Chrome('./downloads/chromedriver')
    url = 'https://translate.google.com/?hl=en&tab=TT&sl=ko&tl=en&op=translate'
    driver.get(url)

    for ko_sent in ko_sent_df:
        # 3. 입력하기
        driver.find_element_by_id('#yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.AxqVh > div.OPPzxe > c-wiz.rm1UF.UnxENd.u3bW4e > span > span > div > textarea').click
        element_ko = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea')
        en_sent_pre = element_ko.send_keys(ko_sent)
        time.sleep(2) ## 2초
        element_en = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]/span[1]/span/span')
        en_sent = element_en.get_text()
        print(en_sent)
        

find_korean(ko_sent_df)