'''
    pdf parser
'''

from datetime import datetime
import timeit
import xlsxwriter
from utils.common_functions import *
from utils.regex_functions import *
from utils.read_pdf import *
from tqdm import tqdm
from word_pos_extractor import *

skip_word = ['서론', '요약', '결론', '본론', '사사']

# Intro 제목
title_regex = re.compile(r'((^\d\.|[Ⅰ|II|Ⅱ|Ⅲ|Ⅳ|Ⅴ]\.)(\d\.){0,})\s{0,}([\D[ㄱ-ㅣ가-힣|a-zA-Z].*)')

# 일반 웹사이트 주소
web_regex = re.compile(r'((http)s{0,1}://)?[\s]{0,1}[-a-z0-9]{0,3}\.{0,1}[-a-z0-9@:%._\\+~#=]{2,256}\.[a-z]{2,4}', re.IGNORECASE)

# 이메일주소
email_regex = re.compile(r'([a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}.{0,1}\w{0,4})', re.IGNORECASE)

# 전화번호 - 021231234(5), (02(2)-123(3)-1234), (02)988-9873, 1234-1234
phone_regex = re.compile(r'[\[<{\(]{0,1}(([\[<{\(]{0,1}[\☎\☏]{0,1}[\s]{0,1}[0-9]{0,3}[}>\)\]]{0,1}\-{0,1}[0-9]{3,4}\-{0,1}[0-9]{3,4})|([0-9]{9,10}))[}>\)\]]{0,1}')

# 날짜 - yyyy.mm.dd | mm.dd.yyyy | dd.mm.yyyy
date_regex = re.compile(r'((\d{4})([\s./-]{0,3})(0[1-9]|1[012]|[1-9])([\s./-]{0,3})(0[1-9]|[12][0-9]|3[0-1]|[1-9])([\s./-]{0,3}))'\
            '|((0[1-9]|1[012]|[1-9])([\s./-]{0,3})(0[1-9]|[12][0-9]|3[0-1]|[1-9])([\s./-]{0,3})(\d{4})([\s./-]{0,3}))'\
            '|((0[1-9]|[12][0-9]|3[0-1]|[1-9])([\s./-]{0,3})(0[1-9]|1[012]|[1-9])([\s./-]{0,3})(\d{4})([\s./-]{0,3}))')


## excel idx 
def excel_index_creator(colum, row_idx):
    colum_idx = colum + str(row_idx)
    return colum_idx
    

def pdf_text_to_excel(pdf_file_list, sub_path):
    if len(pdf_file_list) == 0:
        print('''-----------------------------------------------------------
        PDF파일 없습니다.
        ''')
    else:
        print('''-----------------------------------------------------------
        PDF 작업 시작합니다.
        ''')
        # for time stamp
        timestamp = datetime.now().strftime('%m%d%H%M')
        start = timeit.default_timer()

        error_cnt = 0
        # Open and create each excel file
        workbook = xlsxwriter.Workbook('./results/'  + sub_path  + '/' + sub_path  + '_pdf_'  + timestamp +'.xlsx') # _mustbessossc
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'PATH')
        worksheet.write('B1', 'Raw Data')
        worksheet.write('C1', 'KOR')
        worksheet.write('D1', 'ENG')
        # worksheet.write('E1', 'MOR')
        # worksheet.write('F1', '매캡')
        row_idx = 2
        total_cnt = 0

        completed_log = open(f'./results/' + sub_path  + '/'  + sub_path + '_log_pptx_' + timestamp + '.txt', "w+")
        

        for each_file in tqdm(pdf_file_list):
            try:
                kor_raw_text = ""
                kor_sents = []

                # read pdf files and get as text list
                pdf_text_list = read_pdf_to_text(each_file)

                for line in pdf_text_list:
                    each_line = line.strip()
                    # 숫자만 남은 부분 - header 처리
                    if each_line.isdigit():
                        continue

                    if not each_line or only_char(each_line) or each_line.replace(' ', '') in skip_word \
                            or not isKorean(each_line):  # or len(each_line) < 6:
                        prev_cont = False
                        # continue

                    elif check_fullmatch(web_regex, each_line) or check_fullmatch(email_regex, each_line) \
                            or check_fullmatch(phone_regex, each_line):
                        prev_cont = False
                        # continue

                    else:

                        # list에만 추가
                        if check_fullmatch(title_regex, each_line):
                            prev_cont = False
                            kor_sents.append(each_line)
                            # continue

                        # *로 시작되는 인용문구 처리
                        elif bool(re.compile('^\*').match(each_line)):
                            prev_cont = False
                            kor_sents.append(each_line)

                        # 문장이 아니라 단어들의 나열의 경우 그냥 넣어준다
                        elif words_detect_pos(each_line):
                            kor_sents.append(each_line)
                            prev_cont = False
                            # continue

                        else:
                            # caption handle (stanza exception)
                            caption_regex = re.compile(r'([fig|figure|Fig|Figure|Table]\.)\s{0,}(\d)')
                            each_line = re.sub(caption_regex, r"\1\2", each_line)
                            kor_raw_text += each_line
                            prev_cont = True

                    # 문단이 아닌 경우가 나왔을때 토큰화하여 문장 추가
                    if kor_raw_text and not prev_cont:
                        end_sent_regex = re.compile(r'(다\.)')
                        kor_raw_text = re.sub(end_sent_regex, r"\1 ", kor_raw_text)
                        kor_sents = [*kor_sents, *sentence_tokenizer(kor_raw_text, 'ko')]
                        kor_raw_text = ''

                # last paragraph tokenizing
                kor_raw_text = re.sub(re.compile(r'(다\.)'), r"\1 ", kor_raw_text)
                kor_sents = [*kor_sents, *sentence_tokenizer(kor_raw_text, 'ko')]
                
                # 중복 제거
                kor_sents = set(kor_sents)
                # 총 몇줄인지 확인
                total_cnt += len(kor_sents)
                # print(f'{idx} - {len(raw_sents)}')

                for idx, kor_sent in enumerate(kor_sents):
                    # 한글, 영어가 같이 있는게 아니라면 건너뛰기
                    if isSentKoreanAndEnglish(kor_sent) == False:
                        continue
                    
                    
                    # A. Path 쓰기
                    a_idx =excel_index_creator('A', row_idx)
                    path = each_file.split('/')
                    path =  f'{path[-3]}/{path[-2]}/{path[-1]}/{idx}'
                    worksheet.write(a_idx, path)

                    # raw _sent 형태소 분석 시작
                    # B. Raw Sent 쓰기
                    b_idx =excel_index_creator('B', row_idx)
                    worksheet.write(b_idx, kor_sent)
                    te, ko_words, en_words, mor_match_list_str = find_pattern_show_words(kor_sent)
                    # print('word_matched: ', word_matched)

                    # F. 형태소 분석되는 세세한 것들 쓰기
                    # f_idx =excel_index_creator('F', row_idx)
                    # worksheet.write(f_idx, te)
                    # print(te)
                    

                    for j in range(len(ko_words)):
                        
                        # D의 개수가 1개면 skip
                        en_words[j] = en_words[j].strip(' ')
                        if skip_mored_word(en_words[j]) == True:
                            continue

                        else:
                            # C.  ko_word 쓰기
                            c_idx =excel_index_creator('C', row_idx)
                            worksheet.write(c_idx, ko_words[j])


                            # D.  en_word 쓰기
                            d_idx = excel_index_creator('D', row_idx)
                            worksheet.write(d_idx, en_words[j])
                            

                            # E.  형태소 패턴 쓰기 (확인을 원할때 사용 print or excel에 작성)
                            # Excel 작성
                            # e_idx = excel_index_creator('E', row_idx)
                            
                            # length가 다를때는 일단 넘어가고 
                            # 형태소 어떤 패턴으로 뽑앗는지 확인하기
                            # print해서 확인
                            # if len(ko_words) != len(mor_match_list_str):
                                # continue
                            # length가 같을때는 쓰게 만들기
                            # worksheet.write(e_idx, mor_match_list_str[j])
                            # print(mor_match_list_str[j])
                            
                            # 다음에 쓰여질 줄을 위해서 row_idx += 1
                            row_idx += 1

                # Write Complete log
                path = each_file.split('/')
                path =  f'{path[-3]}/{path[-2]}/{path[-1]}'
                completed_log.write('[DONE READING]' + path + '\n')

            # Write Error log file when docx -> txt
            except Exception as e:
                print('PDF_[ERROR]' + each_file + str(e) +' got ERROR!')
                completed_log.write('[ERROR MESSAGE]' + each_file + str(e) + '\n')

        workbook.close()
        completed_log.close()
        stop = timeit.default_timer()

        print('PDF =====> Raw text to excel DONE (Running Time: ', stop - start, "sec.)")
        print('Total CNT: ', total_cnt)
