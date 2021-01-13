import os
import math
import timeit

from tqdm import tqdm
from datetime import datetime
from xlrd import open_workbook  # for reading

from utils.common_functions import _excel_index_creator
from utils.word_pos_utils import _reg_sent, _isContainKo, _isContainKoT, _isContainEn


def xlsx_text_to_list(xlsx_file_list, sub_path):
    # 파싱한 파일 저장할 사전
    xlsx_filtered_dict = dict()
    xlsx_failed_dict = dict()

    if len(xlsx_file_list) == 0:
        print('''\n-----------------------------------------------------------
        XLSX 없습니다.
        ''')
    else:
        print('''\n-----------------------------------------------------------
        XLSX 작업 시작합니다.
        ''')
        print(f'xlsx는 총 {len(xlsx_file_list)}개 입니다.')
        timestamp = datetime.now().strftime("%m%d%H%M")

        completed_log = open(f'./results/' + sub_path  + '/'  + 'xlsx_completed_log_' + timestamp + '.txt', "w+")
        
        for each_xlsx_file in tqdm(xlsx_file_list):
            file_name =  each_xlsx_file.split('/')[-1]  # 파일명만 빼기
            start = timeit.default_timer() # 작업 시작 시점
            xlsx_sheet_name = ''
            try:
                # xcel 파일 읽기
                load_wb = open_workbook(each_xlsx_file)

                # 엑셀에 포함돼있는 여러 시트들중 하나를 선택하기
                for sheet_name in load_wb.sheet_names():
                    xlsx_sheet_name = sheet_name
                    load_sheet = load_wb.sheet_by_name(sheet_name)

                    xlsx_filtered_list = list() # db 처리 리스트
                    xlsx_failed_list = list() # db 비처리 리스트
 

                    # raw excel의 행의 개수
                    for i in range(load_sheet.nrows):
                        # raw excel의 열의 개수
                        for j in range(load_sheet.ncols):
                            # 셀작업은 한셀씩 오른쪽에서 왼쪽으로 작업이 진행된다
                            cell = str(load_sheet.cell(i, j).value)
                            cell = cell.strip()

                            for sent in cell.split("\n"):
                                filtered_sent = _reg_sent(sent) # 특수문자, km/m 제거

                                # 한국어, 한자, 영어 셋 중 하나라도 없으면 그냥 패스 
                                if _isContainKo(filtered_sent) and _isContainKoT(filtered_sent) and _isContainEn(filtered_sent)== True:
                                    if _isContainKoT(filtered_sent) == True:
                                        xlsx_filtered_list.append(filtered_sent) # db 처리 리스트 추가

                                # 필터로 인해 비처리 할 리스트인지 확인 
                                else:
                                    xlsx_failed_list.append(filtered_sent) # db 비처리 리스트 추가

                    # list로 받은 결과물을 순서대로 dict에 넣어주기
                    xlsx_filtered_dict[file_name] = xlsx_filtered_list
                    xlsx_failed_dict[file_name] = xlsx_failed_list
                    
                    stop = timeit.default_timer() # 작업 끝나는 시점
                    completed_log.write(file_name + '\n') # 완료된 파일 적기
                    completed_log.write('\tSheet 이름' + xlsx_sheet_name + '\n') # 완료된 파일 적기
                    completed_log.write('\t추출 문장 수:' + '\t' + str(len(xlsx_filtered_list)) +'\n')
                    completed_log.write('\tRunning Time:' + '\t' + str(math.ceil(stop - start)) + 'sec\n')
            
            except:
                print('xlsx file error')

        completed_log.close()
    return xlsx_filtered_dict, xlsx_failed_dict