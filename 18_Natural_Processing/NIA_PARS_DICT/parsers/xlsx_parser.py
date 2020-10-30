"""
    excel parser
"""
import os
from xlrd import open_workbook  # for reading
import xlsxwriter  # for writing
from datetime import datetime
import timeit
from itertools import zip_longest
from nltk.tokenize import sent_tokenize

from utils.common_functions import *
from utils.regex_functions import *
from mecab import *


## excel idx 
def excel_index_creator(colum, row_idx):
    colum_idx = colum + str(row_idx)
    return colum_idx



def xlsx_to_excel(xlsx_files, sub_path):
    if len(xlsx_files) == 0:
        print('''-----------------------------------------------------------
        XLSX파일 없습니다.
        ''')
    else:
        print('''-----------------------------------------------------------
        EXCEL 작업 시작합니다.
        ''')
        timestamp = datetime.now().strftime("%m%d%H%M")
        print(" Total excels: ", len(xlsx_files))

        error_cnt = 0

        skip_word = ["영문", "국문", "번역요청표기", "영", "참고", "영문표기", "영어", "연번", "NO",
                    "KOREAN", "ENGLISH", "No.", "KOREAN", "ENG", "KOR", "nope"]

        # for timer
        start = timeit.default_timer()

        # Open and create each excel file
        workbook = xlsxwriter.Workbook('./results/' + sub_path  + '/'  + sub_path  + '_xlsx_' + timestamp +'.xlsx') # _mustbessossc
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'PATH')
        worksheet.write('B1', 'Raw Data')
        worksheet.write('C1', 'KOR')
        worksheet.write('D1', 'ENG')
        worksheet.write('E1', 'MOR')
        worksheet.write('F1', '매캡')
        row_idx = 2
        total_cnt = 0
        # eng_kor = 0
        completed_log = open(f'./results/'  + sub_path  + '/' + sub_path + '_log_xlsx_' + timestamp + '.txt', "w+")

        for file in xlsx_files:
            try:
                load_wb = open_workbook(file)

                # 엑셀에 포함돼있는 여러 시트들중 하나를 선택하기
                for sheet_name in load_wb.sheet_names():

                    load_sheet = load_wb.sheet_by_name(sheet_name)

                    kor_raw_list = [] 
                    kor_sent_list = []

                    # raw excel의 행의 개수
                    for i in range(load_sheet.nrows):
                        # raw excel의 열의 개수
                        for j in range(load_sheet.ncols):
                            # 셀작업은 한셀씩 오른쪽에서 왼쪽으로 작업이 진행된다
                            cell = str(load_sheet.cell(i, j).value)
                            cell = cell.strip()

                            if cell in skip_word or neitherKoNorEn(cell):
                                continue

                            for each_line in cell.split("\n"):
                                if isKorean(each_line):
                                    # Kor/Eng
                                    if isEnglish(each_line):
                                        # [한글 , 영어]
                                        kor_and_eng = split_kor_eng_v2(each_line)
                                        if kor_and_eng[0]:
                                            kor_raw_list.append(kor_and_eng[0])
                                    # Kor
                                    else:
                                        kor_raw_list.append(each_line)

                    # tokenizing
                    for ko_lines in kor_raw_list:
                        kor_sents = sent_tokenize(ko_lines)
                        for ko_sent in kor_sents:
                            kor_sent_list.append(ko_sent)

                kor_sent_list = list(set(kor_sent_list))
                total_cnt += len(kor_sent_list)
                print(len(kor_sent_list))
                
                for idx, kor_sent in enumerate(kor_sent_list):
                    # 한글, 영어가 같이 있는게 아니라면 건너뛰기
                    if isSentKoreanAndEnglish(kor_sent) == False:
                        continue
                    # print(idx, kor_sent)
                    # A. Path 쓰기
                    a_idx =excel_index_creator('A', row_idx)
                    path = file.split('/')
                    path =  f'{path[-3]}/{path[-2]}/{path[-1]}/{idx}'
                    worksheet.write(a_idx, path)

                    # raw _sent 형태소 분석 시작
                    # B. Raw Sent 쓰기
                    b_idx =excel_index_creator('B', row_idx)
                    worksheet.write(b_idx, kor_sent)
                    te, ko_words, en_words, mor_match_list_str = find_pattern_show_words(kor_sent)
                    # print('word_matched: ', word_matched)

                    # F. 쓰기
                    f_idx =excel_index_creator('F', row_idx)
                    worksheet.write(f_idx, te)
                    

                    for j in range(len(ko_words)):
                        
                        # D의 개수가 1개면 skip
                        en_words[j] = en_words[j].strip(' ')
                        if len(en_words[j]) == 1 or en_words[j] in ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vv', 'vii', 'viii', 'x', 'xx', 'ix', 'xiii', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VV', 'VII', 'VIII', 'X', 'XX', 'IX', 'XIII']:
                            continue
                        
                        else:
                            # C.  ko_word 쓰기
                            c_idx =excel_index_creator('C', row_idx)
                            worksheet.write(c_idx, ko_words[j])


                            # D.  en_word 쓰기
                            d_idx = excel_index_creator('D', row_idx)
                            worksheet.write(d_idx, en_words[j])
                            

                            # E.  en_word 쓰기
                            e_idx = excel_index_creator('E', row_idx)
                            # print(row_idx, raw_sent, '\n\t', ko_words[j], '-', en_words[j])
                            # 한-영 짝꿍이 안 맞으면 엑셀에 아예 raw_sent도 입력이 안되서 
                            # length가 다를때는 일단 넘어가고 
                            # 형태소 어떤 패턴으로 뽑앗는지 확인하기

                            if len(ko_words) != len(mor_match_list_str):
                                continue
                            # length가 같을때는 쓰게 만들기
                            worksheet.write(e_idx, mor_match_list_str[j])
                            
                            row_idx += 1
                completed_log.write('[DONE READING]' + file + '\n')

            except Exception as e:
                print("[ERROR]" + file + str(e) + " got ERROR! \n")
                completed_log.write('[ERROR MESSAGE]' + file + str(e) + '\n')

        workbook.close()
        completed_log.close()
        stop = timeit.default_timer()

        print(" ----> Raw excel to excel DONE (Running Time: ", stop - start, " sec.)")
        print(" Total cnt: ", total_cnt)