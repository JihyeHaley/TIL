'''
    docx_mix_parser (병합)
    Word -> HTML raw text -> Excel 으로 변환
    문장 단위 1차 정제 후 엑셀 파일 생성
'''

import timeit
import xlsxwriter
from itertools import zip_longest
from datetime import datetime
from nltk.tokenize import sent_tokenize

from utils.common_functions import *
from utils.regex_functions import *
from mecab import *

stop_word = ['구분', '영문', '국문', '-', '번역', '번역본', '원문', '번역요청', '원본', 'NO', '제목', '타이틀', 'Title',
             '덕수궁관리소', '<참고>', '<영어>', '번역요청(영,일,중간,중번)', '영어:']


## excel idx 
def excel_index_creator(colum, row_idx):
    colum_idx = colum + str(row_idx)
    return colum_idx


# 파일을 돌리는 해당 경로에 결과 엑셀 생성
def docx_mix_to_excel(docx_mix_files, sub_path):
    if len(docx_mix_files) == 0:
        print('''-----------------------------------------------------------
        DOCX Mix 파일 없습니다.
        ''')
    else:
        print('''-----------------------------------------------------------
        DOCX Mix  작업 시작합니다.
        ''')
        timestamp = datetime.now().strftime('%m%d%H%M')
        
        # # path별 문서 list를 가져옴
        # docx_name_lists = get_filename_list(file_path, '.docx')
        print(sub_path + ' Total docx: ', len(docx_mix_files))
        
        workbook = xlsxwriter.Workbook('./results/' + sub_path  + '/' + sub_path  +  '_docx_mix_'  + timestamp +'.xlsx') # _mustbessossc
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'PATH')
        worksheet.write('B1', 'Raw Data')
        worksheet.write('C1', 'KOR')
        worksheet.write('D1', 'ENG')
        worksheet.write('E1', 'MOR')
        worksheet.write('F1', '매캡')
        row_idx = 2
        total_cnt = 0

        completed_log = open(f'./results/'  + sub_path  + '/' + sub_path + '_log_docx_path_' + timestamp + '.txt', "w+")
        # for timer
        start = timeit.default_timer()

        for each_file in docx_mix_files:

            filename = each_file.split('/')[-1]

            # 한/영 병합 문서 파일만 파싱작업
            if filename[-6] == '병': #and filename != '관광-2018한국관광공사-101.마포서교동주민센터__골목여행지도-병.docx':
                
                try:
                    # Word to raw text
                    contents = docx_to_raw_text(each_file, stop_word)

                    ## 각 문서종류별 폴더 안에 파싱된 txt 파일 추가, 폴더가 없으면 생성
                    # pathlib.Path('./' + sub_dir + '_txt').mkdir(parents=True, exist_ok=True)
                    # txt_path = os.path.join(f'./' + sub_dir + '_txt/', filename + ".txt")
                    # all_words = open(txt_path, "w+")

                    kor_raw_list = []
                    kor_sent_list = []

                    for lines in contents:

                        each_line = lines.strip()

                        # Kor or Kor/Eng
                        if not mustEnglish(each_line) and isKorean(each_line):

                            # Kor and Enl - split (영어 두단어 이상 기준)
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


                    # Remove empty string
                    kor_raw_list = list(filter(None, kor_raw_list))
                

                    
                    # raw paragraphs -> sentence tokenize
                    for ko_lines in kor_raw_list:
                        kor_sents = sent_tokenize(regex_cleaner(ko_lines))  # nltk

                        for ko_sent in kor_sents:
                            
                            # 토큰화된 문장에 한/영이 없으면 empty string = no insert
                            if neitherKoNorEn(ko_sent):
                                continue

                            kor_sent_list.append(ko_sent)

                    
                    kor_sent_list = set(kor_sent_list)
                    total_cnt += len(kor_sent_list)

                    for idx, raw_sent in enumerate(kor_sent_list):
                        # 한글, 영어가 같이 있는게 아니라면 건너뛰기
                        if isSentKoreanAndEnglish(raw_sent) == False:
                            continue

                        # A. Path 쓰기
                        a_idx =excel_index_creator('A', row_idx)
                        path = each_file.split('/')
                        path =  f'{path[-3]}/{path[-2]}/{path[-1]}/{idx}'
                        worksheet.write(a_idx, path)

                        # raw _sent 형태소 분석 시작
                        # B. Raw Sent 쓰기
                        b_idx =excel_index_creator('B', row_idx)
                        worksheet.write(b_idx, raw_sent)
                        te, ko_words, en_words, mor_match_list_str = find_pattern_show_words(raw_sent)
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

                    # Write Complete log
                    path = each_file.split('/')
                    path =  f'{path[-3]}/{path[-2]}/{path[-1]}'
                    completed_log.write('[DONE READING]' + path + '\n')
                    

                # Write Error log file when docx -> txt
                except Exception as e:
                    completed_log.write('[ERROR MESSAGE]' + each_file + str(e) + '\n')
                    print('[ERROR]' + filename + str(e) +' got ERROR! \n')

            
        workbook.close()
        completed_log.close()
        stop = timeit.default_timer()
        print(' DOCX_Mix =====> Raw text to excel DONE (Running Time: ', stop - start, "sec.)")
        print(' Total cnt: ', str(total_cnt))