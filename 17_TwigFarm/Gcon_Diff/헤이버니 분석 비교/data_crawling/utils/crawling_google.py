import time


from bs4 import BeautifulSoup
from selenium import webdriver


def google_find_korean(ko_sent_df):
    en_google_sent_df = list()
    total_len = len(ko_sent_df)
    # 2. 웹브라우저 열기
    driver = webdriver.Chrome('/Users/haley/Downloads/chromedriver')
    url = 'https://translate.google.com/?hl=en&tab=TT&sl=ko&tl=en&op=translate'
    

    for idx, ko_sent in enumerate(ko_sent_df):
        # 3. 입력하기
        driver.get(url)
        driver.find_element_by_css_selector('#yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.AxqVh > div.OPPzxe > c-wiz.rm1UF.UnxENd > span > span > div > textarea').click
        element_ko = driver.find_element_by_css_selector('c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.AxqVh > div.OPPzxe > c-wiz.rm1UF.UnxENd > span > span > div > textarea')
        element_ko.send_keys(ko_sent) # 한국어 보내기
        time.sleep(3) ## 5초
        element_en = driver.find_element_by_css_selector('c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.AxqVh > div.OPPzxe > c-wiz.P6w8m.BDJ8fb > div.dePhmb > div > div.J0lOec > span.VIiyi > span > span')# 
        en_sent = element_en.text
        en_google_sent_df.append(en_sent)
        print(f'{idx + 1}/{total_len} - {en_sent}')

    print(en_google_sent_df)  
    return en_google_sent_df



