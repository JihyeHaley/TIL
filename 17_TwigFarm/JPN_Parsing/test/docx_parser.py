'''
    docx_mix_parser (병합)
    Word -> HTML raw text -> Excel 으로 변환
    문장 단위 1차 정제 후 엑셀 파일 생성
'''

import timeit
import xlsxwriter
from itertools import zip_longest
from datetime import datetime

import mammoth


stop_word = []

# mammoth 사용하여 docx raw test parsing
def docx_to_raw_text(file_name):
    with open(file_name, "rb") as docx_file:
        result = mammoth.extract_raw_text(docx_file)
        text = result.value  # The raw text
        messages = result.messages  # Any messages

    contents = text.split("\n")

    contents_prep = []
    for line in contents:
        if '章. ' in line:
            each_line = line.split('.')
            for each_each_line in each_line:
                contents_prep.append(each_each_line)
        else:
            each_line = line.strip()
            contents_prep.append(each_line)

    return contents_prep
file_name = '1. InnoRules Install Guide of Rule Builder.docx'
raw_data = docx_to_raw_text(file_name)
print(raw_data)


workbook = xlsxwriter.Workbook('./1번_데이터.xlsx') # _mustbessossc
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'Japanese')


def excel_index_creator(colum, row_idx):
    colum_idx = colum + str(row_idx)
    return colum_idx

row_idx = 2 
for raw_sent in raw_data:
    idx = excel_index_creator('A', row_idx)

    if raw_sent == '':
        continue
    else:
        input_raw_sent = raw_sent

    worksheet.write(idx, input_raw_sent)
    print(raw_sent)
    print(row_idx)
    row_idx += 1

workbook.close()

# # 파일을 돌리는 해당 경로에 결과 엑셀 생성
# def docx_mix_to_excel(docx_mix_files, sub_path):
#     if len(docx_mix_files) == 0:
#         print('''-----------------------------------------------------------
#         DOCX Mix 파일 없습니다.
#         ''')
#     else:
#         print('''-----------------------------------------------------------
#         DOCX Mix  작업 시작합니다.
#         ''')
#         timestamp = datetime.now().strftime('%m%d%H%M')
        
#         # # path별 문서 list를 가져옴
#         # docx_name_lists = get_filename_list(file_path, '.docx')
        
        
#         workbook = xlsxwriter.Workbook('./results/' + sub_path  + '/' + sub_path  +  '_docx_mix_'  + timestamp +'.xlsx') # _mustbessossc
#         worksheet = workbook.add_worksheet()
#         worksheet.write('A1', 'Raw Data')
#         worksheet.write('B1', 'Japanese')

#         row_idx = 2

#         completed_log = open(f'./results/'  + sub_path  + '/' + sub_path + '_log_docx_path_' + timestamp + '.txt', "w+")
#         docx_mix_word_list_friend = list()
#         # for timer
#         start = timeit.default_timer()

        

#         filename = docx_mix_files

#         try:
#             # Word to raw text
#             contents = docx_to_raw_text(filename, stop_word)

#             ## 각 문서종류별 폴더 안에 파싱된 txt 파일 추가, 폴더가 없으면 생성
#             # pathlib.Path('./' + sub_dir + '_txt').mkdir(parents=True, exist_ok=True)
#             # txt_path = os.path.join(f'./' + sub_dir + '_txt/', filename + ".txt")
#             # all_words = open(txt_path, "w+")

#             kor_raw_list = []
#             kor_sent_list = []

#             for lines in contents:

#                 each_line = lines.strip()

#                 # Kor or Kor/Eng
#                 if not mustEnglish(each_line) and isKorean(each_line):

#                     # Kor and Enl - split (영어 두단어 이상 기준)
#                     if isEnglish(each_line):
#                         kor_and_eng = split_kor_eng(each_line)
#                         for both_lang in kor_and_eng:
#                             if both_lang.strip() and mustEnglish(both_lang):
#                                 eng_raw_list.append(both_lang)
#                             elif both_lang.strip() and not mustEnglish(both_lang):
#                                 kor_raw_list.append(both_lang)

#                     else:
#                         # 한글 or 영어없는 공백,숫자,특수문자
#                         kor_raw_list.append(each_line)


#             # Remove empty string
#             kor_raw_list = list(filter(None, kor_raw_list))
        

            
#             # raw paragraphs -> sentence tokenize
#             for ko_lines in kor_raw_list:
#                 kor_sents = sent_tokenize(regex_cleaner(ko_lines))  # nltk

#                 for ko_sent in kor_sents:
                    
#                     # 토큰화된 문장에 한/영이 없으면 empty string = no insert
#                     if neitherKoNorEn(ko_sent):
#                         continue

#                     kor_sent_list.append(ko_sent)

#                 # 중복 제거
#             kor_sent_list_full = list()
#             for sent in kor_sent_list:
#                 if sent not in kor_sent_list_full:
#                     kor_sent_list_full.append(sent)
#             # 총 몇줄인지 확인
#             total_cnt += len(kor_sent_list_full)
#             # print(f'{total_idx} - {len(kor_sent_list)}')

#             for idx, raw_sent in enumerate(kor_sent_list_full):
#                 # 한글, 영어가 같이 있는게 아니라면 건너뛰기
#                 if isSentKoreanAndEnglish(raw_sent) == False:
#                     continue

#                 # A. Path 쓰기
#                 a_idx =excel_index_creator('A', row_idx)
#                 path = each_file.split('/')
#                 path =  f'{path[-3]}/{path[-2]}/{path[-1]}/{idx}'
#                 worksheet.write(a_idx, path)

#                 # raw _sent 형태소 분석 시작
#                 # B. Raw Sent 쓰기
#                 b_idx =excel_index_creator('B', row_idx)
#                 worksheet.write(b_idx, raw_sent)
#                 ko_words, en_words= find_pattern_show_words(raw_sent)
                


#                 for j in range(len(ko_words)):
#                     # 중복 방지
#                     if [ko_words[j], en_words[j]] in docx_mix_word_list_friend:
#                         continue
#                     else:
#                         docx_mix_word_list_friend.append([ko_words[j], en_words[j]])
#                         # D의 개수가 1개면 skip
#                         en_words[j] = en_words[j].strip(' ')
#                         if skip_mored_word(en_words[j]) == True:
#                             continue
#                         else:
#                             # C.  ko_word 쓰기
#                             c_idx =excel_index_creator('C', row_idx)
#                             worksheet.write(c_idx, ko_words[j])


#                             # D.  en_word 쓰기
#                             d_idx = excel_index_creator('D', row_idx)
#                             worksheet.write(d_idx, en_words[j])
                            
#                             row_idx += 1

#             # Write Complete log
#             path = each_file.split('/')
#             path =  f'{path[-3]}/{path[-2]}/{path[-1]}'
#             completed_log.write('[DONE READING]' + path + '\n')
            

#         # Write Error log file when docx -> txt
#         except Exception as e:
#             completed_log.write('[ERROR MESSAGE]' + each_file + str(e) + '\n')
#             print('[ERROR]' + filename + str(e) +' got ERROR! \n')

        
#         workbook.close()
#         completed_log.close()
#         stop = timeit.default_timer()
#         print(' DOCX_Mix =====> Raw text to excel DONE (Running Time: ', stop - start, "sec.)")
#         print(' Total cnt: ', str(total_cnt))