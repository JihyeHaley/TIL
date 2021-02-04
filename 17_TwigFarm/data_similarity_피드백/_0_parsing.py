import time
import timeit
import random
import xlsxwriter
import pandas as pd

from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver


from _1_import_excel import _import_df
from _1_en_crawling import google_find_korean, papago_find_korean, google, papago
from _2_mor_analyze import _work_start_tokenizer
from _3_similarity_cal import _calc_distance, _check_similarity
from _4_word_diff_check import _diff_word_dark
from common_functions import _excel_index_creator

# 엑셀에 쓰기
def write_in_the_excel():

    timestamp = datetime.now().strftime('%m%d%H%M')

    # A. 엑셀 쓰기
    workbook = xlsxwriter.Workbook('./results/' +  '_' + timestamp + '_엑셀.xlsx')

    worksheet = workbook.add_worksheet()

    cell_yellow = workbook.add_format()
    cell_yellow.set_pattern(1)
    cell_yellow.set_bg_color(('yellow'))

    worksheet.write('A1', 'No')
    worksheet.write('B1', '원문', cell_yellow)
    worksheet.write('C1', '구글', cell_yellow)
    worksheet.write('D1', '유사도', cell_yellow)
    worksheet.write('E1', '파파고', cell_yellow)
    worksheet.write('F1', '표현검색', cell_yellow)
    
    row_idx = 2

    # B. 파일 불러오기 
    ko_df = _import_df()

    # C. 셀레늄 작동 
    google_driver = webdriver.Chrome('/Users/haley/Downloads/chromedriver')
    google_url = 'https://translate.google.com/?hl=en&tab=TT&sl=ko&tl=en&op=translate'
    
    papago_driver = webdriver.Chrome('/Users/haley/Downloads/chromedriver')
    papago_url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%EB%B2%88%EC%97%AD'

    sleep_time = random.randrange(3,5)
    time.sleep(6) ## 5초

    # D. 한 줄씩 -> 작성하기
    for idx, ko_sent in enumerate(ko_df):
        print(ko_sent)

        # a. 번역된 데이터 가져오기
        
        google_driver.get(google_url)
        google_driver.find_element_by_css_selector('#yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.AxqVh > div.OPPzxe > c-wiz.rm1UF.UnxENd > span > span > div > textarea').click
        element_ko = google_driver.find_element_by_css_selector('c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.AxqVh > div.OPPzxe > c-wiz.rm1UF.UnxENd > span > span > div > textarea')
        element_ko.send_keys(ko_sent) # 한국어 보내기
        time.sleep(sleep_time) 
        element_en = google_driver.find_element_by_css_selector('c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.AxqVh > div.OPPzxe > c-wiz.P6w8m.BDJ8fb > div.dePhmb > div > div.J0lOec > span.VIiyi > span > span')# 
        google_en_sent = element_en.text

        papago_driver.get(papago_url)
        papago_driver.find_element_by_css_selector('#_au_translator > div.tlans_box > div.txt_box._input > div.txt_area._view > textarea').click
        element_ko = papago_driver.find_element_by_css_selector('#_au_translator > div.tlans_box > div.txt_box._input > div.txt_area._view > textarea')
        element_ko.send_keys(ko_sent) # 한국어 보내기
        time.sleep(sleep_time) 
        element_en = papago_driver.find_element_by_css_selector('#_au_translator > div.tlans_box > div.txt_box.rt._output.on > div.txt_area._view > p') 
        papago_en_sent = element_en.text


        # b. 형태소
        google_words, google_mor = _work_start_tokenizer(google_en_sent) # 구글
        papago_words, papago_mor = _work_start_tokenizer(papago_en_sent) # 파파고


        # c. 유사도 측정
        similarity_price = _check_similarity(google_words, papago_words) # 문장 넘기기
        a_idx = _excel_index_creator('A', row_idx) # No.
        b_idx = _excel_index_creator('B', row_idx) # 원문
        c_idx = _excel_index_creator('C', row_idx) # 구글
        d_idx = _excel_index_creator('D', row_idx) # 유사도
        e_idx = _excel_index_creator('E', row_idx) # 파파고
        f_idx = _excel_index_creator('F', row_idx) # 표현검색
        
        worksheet.write(a_idx, str(row_idx - 1)) # a. No.
        worksheet.write(b_idx, str(ko_sent)) # b. 원문
        worksheet.write(c_idx, str(similarity_price[-1])) # c. 유사도

        # 유사도 정도에 따라서 분석
        # 정제 탈락 (0, 10이상, 단어 길이 3 미만)
        if similarity_price[-1] >= 10 or similarity_price[-1] == 0 or len(google_words) <= 3 or len(papago_words) <= 3:
            worksheet.write(b_idx, str(google_en_sent)) # 구글
            worksheet.write(d_idx, str(papago_en_sent)) # 파파고

        # 정제 성공 (유사도 1-9)
        elif similarity_price[-1] >= 1 and similarity_price[-1] <= 9:
            g_sent, p_sent = _diff_word_dark(google_words,papago_words)
            worksheet.write(b_idx, str(g_sent), cell_yellow) # 구글
            worksheet.write(d_idx, str(p_sent), cell_yellow) # 파파고 
        print(google_words)
        print(papago_words)
        

        row_idx += 1
    print(f'row_idx : {row_idx}')
    print('done')
    workbook.close()

write_in_the_excel()
