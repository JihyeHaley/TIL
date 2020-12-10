"""
    docx_separate parser

    Notes:
    1. 절대경로 말고 상대경로로 맞춰서 사용해주세요.
    2. docx_separate_to_excel 다시 작성해주세요. parameter는 dict로 받습니다.
        docx_separte_dict = {'한': [filename1, filename2, ..],
                             '영': [filename1, filename2, ..],
                             '병': [filename1, filename2, ..],
                             '양': [filename1, filename2, ..]}

"""

import timeit
import xlsxwriter
from itertools import zip_longest
from datetime import datetime
from nltk.tokenize import sent_tokenize

from utils.common_functions import *
from utils.regex_functions import *


stop_word = ['구분', '영문', '국문', '-', '번역', '번역본', '원문', '번역요청', '원본', 'NO', '제목', '타이틀', 'Title',
             '덕수궁관리소', '<참고>', '<영어>', '번역요청(영,일,중간,중번)', '영어:']



# ko 파일과 en 파일을 짝을 찾아주기 위한 함수
def file_matching(docx_ko_files, docx_en_files):
    check_matching_dict = {}

    for ko_each_file in docx_ko_files:
        change_file_name(ko_each_file)
        # 딕셔너리에 처음 등장한 경우는 1로 초기화
        if ko_each_file[:-6] not in check_matching_dict.keys():
            # 파일이름(경로포함)에서 "한.docx" 를 제외하고 딕셔너리에 담는다
            check_matching_dict[ko_each_file[:-6]] = 1
        # 딕셔너리에 이미 존재하는 경우 개수를 올려준다
        else:
            check_matching_dict[ko_each_file[:-6]] += 1
    for en_each_file in docx_en_files:
        change_file_name(en_each_file)
        if en_each_file[:-6] not in check_matching_dict.keys():
            check_matching_dict[en_each_file[:-6]] = 1
        else:
            check_matching_dict[en_each_file[:-6]] += 1

    return check_matching_dict


def docx_separate_to_excel(docx_separate_dict):

    timestamp = datetime.now().strftime("%m%d%H%M")

    # en / ko / 통합 파일 리스트를 나누기.
    # ========> docx_separate_dict key 값으로 사용해주세요
    ##############################################################

    # ko 파일과 en 파일 pair를 맞춰주기.
    # {"경로/파일이름(한.docx는 제외된 상태)" : 1 or 2 .. } 이런 식으로 결과가 나온다
    #check_matching_dict = file_matching(docx_ko_files, docx_en_files)

    # Open and create excel file
    workbook = xlsxwriter.Workbook("excel_" + timestamp + ".xlsx")
    worksheet = workbook.add_worksheet()
    worksheet.write("B1", "KOR")
    worksheet.write("C1", "ENG")
    row_idx = 2

    # Open log files: record the order of file names
    completed_log = open(f"./log_" + timestamp + ".txt", "w+")
    inte_read_cnt = 0
    sep_read_cnt = 0
    not_pair_cnt = 0
    error_cnt = 0

    # for timer
    start = timeit.default_timer()

    # 통합 파일 파싱작업 시작.
    for each_file in docx_inte_files:

        filename = each_file.split("/")[-1]

        inte_read_cnt += 1
        try:
            # 문서간 구분을 위해 추가
            worksheet.write("A" + str(row_idx), ">" * 10)
            worksheet.write("B" + str(row_idx), ">" * 10 + filename)
            row_idx += 1

            # Word to raw text
            contents = docx_to_raw_text(each_file)

            ## 각 문서종류별 폴더 안에 파싱된 txt 파일 추가, 폴더가 없으면 생성
            # pathlib.Path('./' + sub_dir + '_txt').mkdir(parents=True, exist_ok=True)
            # txt_path = os.path.join(f'./' + sub_dir + '_txt/', filename + ".txt")
            # all_words = open(txt_path, "w+")

            kor_raw_list = []
            eng_raw_list = []

            kor_sent_list = []
            eng_sent_list = []

            for lines in contents:
                each_line = lines.strip()

                if not mustEnglish(each_line) and isKorean(each_line):
                    if isEnglish(each_line):
                        kor_and_eng = split_kor_eng(each_line)
                        for both_lang in kor_and_eng:
                            if both_lang.strip() and mustEnglish(both_lang):
                                eng_raw_list.append(both_lang)
                            elif both_lang.strip() and not mustEnglish(both_lang):
                                kor_raw_list.append(both_lang)

                    else:
                        # 한글 or 영어없는 공백,숫자,특수문자
                        kor_raw_list.append(each_line)

                # 영어
                elif mustEnglish(each_line) and not isKorean(each_line):
                    eng_raw_list.append(each_line)

            # Remove empty string
            kor_raw_list = list(filter(None, kor_raw_list))
            eng_raw_list = list(filter(None, eng_raw_list))

            # raw paragraphs -> sentence tokenize
            for ko_lines in kor_raw_list:
                kor_sents = sent_tokenize(strip_regex_all(ko_lines))  # nltk

                for ko_sent in kor_sents:
                    # # 토큰화된 문장에 한/영이 없으면 empty string = no insert
                    # if neitherKoNorEn(ko_sent):
                    #     continue
                    kor_sent_list.append(ko_sent)

            for en_lines in eng_raw_list:
                eng_sents = sent_tokenize(strip_regex_all(en_lines))  # nltk

                for en_sent in eng_sents:
                    # # 토큰화된 문장에 한/영이 없으면 empty string = no insert
                    # if neitherKoNorEn(en_sent):
                    #     continue
                    eng_sent_list.append(en_sent)
            # ----------------------------------------

            # Write Excel file
            for ko, en in zip_longest(kor_sent_list, eng_sent_list, fillvalue=" "):
                worksheet.write("B" + str(row_idx), str(ko))
                worksheet.write("C" + str(row_idx), str(en))
                row_idx += 1

            # Write Complete log
            completed_log.write("[DONE READING]" + filename + " \n\n")

        # Write Error log file when docx -> txt
        except Exception as e:
            completed_log.write("[ERROR]" + filename + ".txt got ERROR! \n")
            completed_log.write("[ERROR MESSAGE]" + str(e) + "\n")
            print("[ERROR]" + filename + " got ERROR! \n")
            error_cnt += 1

    # ko , en로 분리된 파일 파싱 작업 시작.
    for each_file, num in check_matching_dict.items():
        filename = each_file.split("/")[-1]
        # 같은 이름의 파일이 2개 일경우.
        if num == 2:
            ko_each_file = each_file + "한.docx"
            en_each_file = each_file + "영.docx"
            sep_read_cnt += 2
            try:
                # 문서간 구분을 위해 추가
                worksheet.write("A" + str(row_idx), ">" * 10)
                worksheet.write("B" + str(row_idx), ">" * 10 + filename)
                row_idx += 1

                # Word to raw text
                # 한글 파일, 영문 파일 나뉘어있으므로 나누는 작업은 생략. 바로 정제를 시작한다.
                ko_contents = docx_to_raw_text(ko_each_file, stop_word)
                en_contents = docx_to_raw_text(en_each_file, stop_word)

                ## 각 문서종류별 폴더 안에 파싱된 txt 파일 추가, 폴더가 없으면 생성
                # pathlib.Path('./' + sub_dir + '_txt').mkdir(parents=True, exist_ok=True)
                # txt_path = os.path.join(f'./' + sub_dir + '_txt/', filename + ".txt")
                # all_words = open(txt_path, "w+")

                kor_sent_list = []
                eng_sent_list = []

                # raw paragraphs -> sentence tokenize
                for ko_lines in ko_contents:
                    kor_sents = sent_tokenize(strip_regex_all(ko_lines))  # nltk

                    for ko_sent in kor_sents:

                        # 토큰화된 문장에 한/영이 없으면 empty string = no insert
                        if neitherKoNorEn(ko_sent):
                            continue

                        kor_sent_list.append(ko_sent)

                for en_lines in en_contents:
                    eng_sents = sent_tokenize(strip_regex_all(en_lines))  # nltk

                    for en_sent in eng_sents:

                        # 토큰화된 문장에 한/영이 없으면 empty string = no insert
                        if neitherKoNorEn(en_sent):
                            continue

                        eng_sent_list.append(en_sent)
                # ----------------------------------------

                # Write Excel file
                for ko, en in zip_longest(kor_sent_list, eng_sent_list, fillvalue=" "):
                    worksheet.write("B" + str(row_idx), str(ko))
                    worksheet.write("C" + str(row_idx), str(en))
                    row_idx += 1

                # Write Complete log
                completed_log.write("[DONE READING]" + filename + " \n\n")

            # Write Error log file when docx -> txt
            except Exception as e:
                completed_log.write("[ERROR]" + filename + ".txt got ERROR! \n")
                completed_log.write("[ERROR MESSAGE]" + str(e) + "\n")
                print("[ERROR]" + filename + " got ERROR! \n")
                error_cnt += 1
        # 같은이름의 파일이 2개가 아닐경우
        else:
            print("not pair!!" + filename)
            not_pair_cnt += num

    completed_log.close()
    workbook.close()

    stop = timeit.default_timer()

    print(" ----> Raw text to excel DONE (Running Time: ", stop - start, " sec.)")
    print(
        " 통합 파일 수: "
        + str(inte_read_cnt)
        + " , "
        + " 한/영 파일 수:"
        + str(sep_read_cnt)
        + " 짝을 못찾은 파일수: "
        + str(not_pair_cnt)
        + " (out of total "
        + str(len(docx_separate_dict))
        + " files)"
    )
    print("Total ERROR: ", error_cnt)
