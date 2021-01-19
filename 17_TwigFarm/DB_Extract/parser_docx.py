import math
import timeit

from tqdm import tqdm
from datetime import datetime
from xlrd import open_workbook  # for reading

from utils.common_functions import _excel_index_creator
from utils.docx_utils import _read_docx_to_text
from utils.word_pos_utils import _reg_sent, _isContainKo, _isContainKoT, _isContainEn


stop_word = ['구분', '영문', '국문', '-', '번역', '번역본', '원문', '번역요청', '원본', 'NO', '제목', '타이틀', 'Title',
             '덕수궁관리소', '<참고>', '<영어>', '번역요청(영,일,중간,중번)', '영어:']


# 파일을 돌리는 해당 경로에 결과 엑셀 생성
def docx_text_to_list(docx_file_list, sub_path):
    # 파싱한 파일 저장할 사전
    docx_filtered_dict = dict()
    docx_failed_dict = dict()

    if len(docx_file_list) == 0:
        print('''\n-----------------------------------------------------------
        DOCX 없습니다.
        ''')
    else:
        print('''\n-----------------------------------------------------------
        DOCX 작업 시작합니다.
        ''')
        print(f'DOCX는 총 {len(docx_file_list)}개 입니다.')
        timestamp = datetime.now().strftime("%m%d%H%M")
        completed_log = open(f'./results/'  + sub_path  + '/'  + 'docx_completed_log_' +timestamp + '.txt', "w+")


        for each_docx_file in tqdm(docx_file_list):
            file_name =  each_docx_file.split('/')[-1]  # 파일명만 빼기
            start = timeit.default_timer() # 작업 시작 시점

            try:
                # docx 파일 읽기 list 형태
                docx_text_list = _read_docx_to_text(each_docx_file, stop_word)

                docx_filtered_list = list() # db 처리 리스트
                docx_failed_list = list() # db 비처리 리스트

                
                for sent in docx_text_list:
                    filtered_sent = _reg_sent(sent) # 특수문자, km/m 제거

                    # 한국어, 한자, 영어 셋 중 하나라도 없으면 그냥 패스 
                    if _isContainKo(filtered_sent) and _isContainKoT(filtered_sent) and _isContainEn(filtered_sent)== True:
                        if _isContainKoT(filtered_sent) == True:
                            docx_filtered_list.append(filtered_sent) # db 처리 리스트 추가

                        # 필터로 인해 비처리 할 리스트인지 확인 
                    else:
                        docx_failed_list.append(filtered_sent) # db 비처리 리스트 추가
            
                # Remove empty string
                docx_filtered_list = list(filter(None, docx_filtered_list))
                docx_failed_list = list(filter(None, docx_failed_list))

                # list로 받은 결과물을 순서대로 dict에 넣어주기
                docx_filtered_dict[file_name] = docx_filtered_list
                docx_failed_dict[file_name] = docx_failed_list


                stop = timeit.default_timer() # 작업 끝나는 시점
                completed_log.write(file_name + '\n') # 완료된 파일 적기
                completed_log.write('\t전체 문장 수:' + '\t' + str(len(docx_text_list)) +'\n')
                completed_log.write('\t추출 문장 수:' + '\t' + str(len(docx_filtered_list)) +'\n')
                completed_log.write('\t비추출 문장 수:' + '\t' + str(len(docx_failed_list)) +'\n')
                completed_log.write('\tRunning Time:' + '\t' + str(math.ceil(stop - start)) + 'sec\n')
            
            except:
                print('docx file error')

        completed_log.close()
    return docx_filtered_dict, docx_failed_dict