# # Ver 1 - reuqests
# import requests
# webpage = requests.get('https://dreamin.career/dreamhaus')
# print(webpage.text)


# # Ver 2 - BeautifulSoup
# # Example with 서울 외국어 표기사전
# import requests
# from bs4 import BeautifulSoup
# webpage = requests.get('https://dictionary.seoul.go.kr/spelling/dictionary')
# soup = BeautifulSoup(webpage.content, 'html.parser')
# # print(soup.find_all(attrs = {'class': ''}))
# print(soup.select('.one_depth'))

# Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
path = "/Users/jihyeoh/chromedriver"
driver = webdriver.Chrome(path)
# 서울 외국어 표기작업
driver.get('https://dictionary.seoul.go.kr/spelling/dictionary')
# array_idx = [3, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# for i in array_idx:
#     search_box = driver.find_element_by_class_name(f'main_array{i}').click()
#     # detail = driver.find_elements_by_class_name('select')
#     zaijian = driver.find_element_by_class_name('btn_close').click()
array_idx = 3
search_box = driver.find_element_by_class_name(f'main_array{array_idx}').click()
detail = driver.find_elements_by_class_name('div.two_depth > select')
print(detail)
for _ in detail:
    driver.find_element_by_class_name(_).click()

# for _ in search_box:
#     print(_.text.strip())
