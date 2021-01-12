from datetime import datetime
import timeit
import xlsxwriter
from tqdm import tqdm
import re

from utils.common_functions import _excel_index_creator, _reg_sent
from utils.pdf_utils import _isContainKo, _isContainKoT, _isContainEn, _read_pdf_to_text


def _pdf_text_to_list(pdf_file_list):
    if len(pdf_file_list) == 0:
        print('''-----------------------------------------------------------
        PDF파일 없습니다.
        ''')
    else:
        print('''-----------------------------------------------------------
        PDF 작업 시작합니다.
        ''')
        print(f'PDF는 총 {len(pdf_file_list)}개 입니다.')
        
        for each_file in tqdm(pdf_file_list):
            start = timeit.default_timer() # 작업 시작 시점

            # pdf 파일 읽기 as List형태
            pdf_text_list = _read_pdf_to_text(each_file) 

            pdf_filtered_list = list() # db 처리 리스트
            pdf_failed_list = list() # db 비처리 리스트

            # pdf 파일 분류(처리/비처리)
            for sent in pdf_text_list:
                filtered_sent = _reg_sent(sent) # 특수문자, km/m 제거

                # 한국어, 한자, 영어 셋 중 하나라도 없으면 그냥 패스 
                if _isContainKo(filtered_sent) and _isContainKoT(filtered_sent) and _isContainEn(filtered_sent)== True:
                    if _isContainKoT(filtered_sent) == True:
                        pdf_filtered_list.append(filtered_sent) # db 처리 리스트 추가
                else:
                    pdf_failed_list.append(filtered_sent) # db 비처리 리스트 추가

        
            stop = timeit.default_timer() # 작업 끝나는 시점
            print(f'pdf_parser Running Time: {stop - start} sec')
            print(f'전체 문장 수: {len(pdf_text_list)}')
            print(f'추출 문장 수: {len(pdf_filtered_list)}')

    return pdf_filtered_list, pdf_failed_list
            

        
