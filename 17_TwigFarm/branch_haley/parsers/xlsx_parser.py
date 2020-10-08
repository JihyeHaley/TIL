'''
    excel parser
'''

from xlrd import open_workbook  # for reading
import xlsxwriter               # for writing
from datetime import datetime
import timeit
from itertools import zip_longest
from nltk.tokenize import sent_tokenize

from utils.common_functions import *
from utils.regex_functions import *


def xlsx_to_excel(xlsx_lists):


    timestamp = datetime.now().strftime("%m%d%H%M")
    completed_log = open(f"./log_" + timestamp + ".txt", "w+")
    error_cnt = 0


    skip_word = ["영문", "국문", "번역요청표기", "영", "참고", "영문표기", "영어", "연번",
                 "NO", "KOREAN", "ENGLISH", "No.", "KOREAN", "ENG", "KOR", "nope"]

    # for timer
    start = timeit.default_timer()

    # ==============> !!!!!!!!!!! xlsx_dict.values() 확인해주세요.
    for file in xlsx_lists:
        file_name = file.split("/")[-1][:-5]

        # 각 raw excel 파일을 위해 매번 새로운 excel 파일을 만든다.
        workbook = xlsxwriter.Workbook('./results/' + file_name + ".xlsx")
        worksheet = workbook.add_worksheet()
        worksheet.write("B1", "KOR")
        worksheet.write("C1", "ENG")
        row_idx = 2

        try:
            load_wb = open_workbook(file)

            # 엑셀에 포함돼있는 여러 시트들중 하나를 선택하기
            for sheet_name in load_wb.sheet_names():
                file_name = file_name + "/" + sheet_name
                worksheet.write("A" + str(row_idx), ">" * 10)
                worksheet.write("B" + str(row_idx), ">" * 10 + file_name)
                row_idx += 1

                load_sheet = load_wb.sheet_by_name(sheet_name)

                kor_raw_list = []
                eng_raw_list = []

                kor_sent_list = []
                eng_sent_list = []

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
                                    if kor_and_eng[1]:
                                        eng_raw_list.append(kor_and_eng[1])
                                # Kor
                                else:
                                    kor_raw_list.append(each_line)

                            # eng or 의미없는 문자열
                            elif not isKorean(each_line):
                                eng_raw_list.append(each_line)

                # tokenizing
                for ko_lines in kor_raw_list:
                    kor_sents = sent_tokenize(strip_regex_all(ko_lines))
                    for ko_sent in kor_sents:
                        # if neitherKoNorEn(ko_sent):
                        #     continue
                        kor_sent_list.append(ko_sent)

                for en_lines in eng_raw_list:
                    eng_sents = sent_tokenize(strip_regex_all(en_lines))
                    for en_sent in eng_sents:
                        # if neitherKoNorEn(en_sent):
                        #     continue
                        eng_sent_list.append(en_sent)

                for ko, en in zip_longest(kor_sent_list, eng_sent_list, fillvalue=""):
                    if not ko and not en:
                        continue
                    worksheet.write("B" + str(row_idx), ko)
                    worksheet.write("C" + str(row_idx), en)
                    row_idx += 1

                completed_log.write("[DONE READING]" + file_name + " \n\n")

        except Exception as e:
            completed_log.write('[ERROR]' + file_name + '.txt got ERROR! \n')
            completed_log.write('[ERROR MESSAGE]' + str(e) + '\n')
            print('[ERROR]' + file_name + ' got ERROR! \n')
            error_cnt += 1

    completed_log.close()
    workbook.close()

    stop = timeit.default_timer()

    print(" ----> Raw excel to excel DONE (Running Time: ", stop - start, " sec.)")
    print(" Total ERROR: ", error_cnt)
