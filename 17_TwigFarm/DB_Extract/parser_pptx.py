import timeit

from tqdm import tqdm
from datetime import datetime

from utils.common_functions import _excel_index_creator
from utils.pptx_utils import _read_pptx_to_text
from utils.word_pos_utils import _reg_sent, _isContainKo, _isContainKoT, _isContainEn


def pptx_text_to_list(pptx_file_list, sub_path):
    # 파싱한 파일 저장할 사전
    pptx_filtered_dict = dict()
    pptx_failed_dict = dict()

    if len(pptx_file_list) == 0:
        print('''\n-----------------------------------------------------------
        PPTX 없습니다.
        ''') 
    else:
        print('''\n-----------------------------------------------------------
        PPTX 작업 시작합니다.
        ''')
        
        print(f'pptx는 총 {len(pptx_file_list)}개 입니다.')
        timestamp = datetime.now().strftime("%m%d%H%M")
        completed_log = open(f'./results/'  + sub_path  + '/'  + 'pptx_completed_log_' +timestamp + '.txt', "w+")

        for each_pptx_file in tqdm(pptx_file_list):
            file_name =  each_pptx_file.split('/')[-1]  # 파일명만 빼기
            start = timeit.default_timer() # 작업 시작 시점
            
            try:
                pptx_text_list = _read_pptx_to_text(each_pptx_file)


                pptx_filtered_list = list() # db 처리 리스트
                pptx_failed_list = list() # db 비처리 리스트

                # pptx 파일 분류(처리/비처리)
                for sent in pptx_text_list:
                    filtered_sent = _reg_sent(sent) # 특수문자, km/m 제거

                    # 한국어, 한자, 영어 셋 중 하나라도 없으면 그냥 패스 
                    if _isContainKo(filtered_sent) and _isContainKoT(filtered_sent) and _isContainEn(filtered_sent)== True:
                        if _isContainKoT(filtered_sent) == True:
                            pptx_filtered_list.append(filtered_sent) # db 처리 리스트 추가
                    
                    # 필터로 인해 비처리 할 리스트인지 확인 
                    else:
                        pptx_failed_list.append(filtered_sent) # db 비처리 리스트 추가

                # Remove empty string
                pptx_failed_list = list(filter(None, pptx_failed_list))
                pptx_failed_list = list(filter(None, pptx_failed_list))

                # list로 받은 결과물을 순서대로 dict에 넣어주기
                pptx_filtered_dict[file_name] = pptx_filtered_list
                pptx_failed_dict[file_name] = pptx_failed_list
                
                
                stop = timeit.default_timer() # 작업 끝나는 시점
                print(f'{file_name} pptx_parser Running Time: {stop - start} sec')
                print(f'전체 문장 수: {len(pptx_text_list)}')
                print(f'추출 문장 수: {len(pptx_filtered_list)}')
                completed_log.write(file_name+'\n') # 완료된 파일 적기
                            
            except:
                print('pptx file error')

        completed_log.close()
    return pptx_filtered_dict, pptx_failed_dict
            
