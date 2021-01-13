import timeit

from tqdm import tqdm
from datetime import datetime

from utils.common_functions import _excel_index_creator
from utils.pdf_utils import _read_pdf_to_text
from utils.word_pos_utils import _reg_sent, _isContainKo, _isContainKoT, _isContainEn


def pdf_text_to_list(pdf_file_list, sub_path):
    # 파싱한 파일 저장할 사전
    pdf_filtered_dict = dict()
    pdf_failed_dict = dict()
    
    if len(pdf_file_list) == 0:
        print('''\n-----------------------------------------------------------
        PDF 없습니다.
        ''')
    else:
        print('''\n-----------------------------------------------------------
        PDF 작업 시작합니다.
        ''')
        print(f'PDF는 총 {len(pdf_file_list)}개 입니다.')
        timestamp = datetime.now().strftime("%m%d%H%M")
        
        completed_log = open(f'./results/'  + sub_path  + '/'  + 'pdf_completed_log_' +timestamp + '.txt', "w+")

        for each_pdf_file in tqdm(pdf_file_list):
            file_name =  each_pdf_file.split('/')[-1]  # 파일명만 빼기
            start = timeit.default_timer() # 작업 시작 시점

            try:
                # pdf 파일 읽기 as List형태
                pdf_text_list = _read_pdf_to_text(each_pdf_file) 

                pdf_filtered_list = list() # db 처리 리스트
                pdf_failed_list = list() # db 비처리 리스트

                # pdf 파일 분류(처리/비처리)
                for sent in pdf_text_list:
                    filtered_sent = _reg_sent(sent) # 특수문자, km/m 제거

                    # 한국어, 한자, 영어 셋 중 하나라도 없으면 그냥 패스 
                    if _isContainKo(filtered_sent) and _isContainKoT(filtered_sent) and _isContainEn(filtered_sent)== True:
                        if _isContainKoT(filtered_sent) == True:
                            pdf_filtered_list.append(filtered_sent) # db 처리 리스트 추가
                    
                    # 필터로 인해 비처리 할 리스트인지 확인 
                    else:
                        pdf_failed_list.append(filtered_sent) # db 비처리 리스트 추가

                # Remove empty string
                pdf_failed_list = list(filter(None, pdf_failed_list))
                pdf_failed_list = list(filter(None, pdf_failed_list))

                # list로 받은 결과물을 순서대로 dict에 넣어주기
                pdf_filtered_dict[file_name] = pdf_filtered_list
                pdf_failed_dict[file_name] = pdf_failed_list


                stop = timeit.default_timer() # 작업 끝나는 시점
                print(f'{file_name} pdf_parser Running Time: {stop - start} sec')
                print(f'전체 문장 수: {len(pdf_text_list)}')
                print(f'추출 문장 수: {len(pdf_filtered_list)}')
                completed_log.write(file_name+'\n') # 완료된 파일 적기
            
            except:
                print('pdf file error')

        completed_log.close()
    return pdf_filtered_dict, pdf_failed_dict
            

        
