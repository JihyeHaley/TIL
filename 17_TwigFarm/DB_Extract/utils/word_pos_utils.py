# import MeCab
from konlpy.tag import Mecab
from datetime import datetime
import timeit
import re


# 특수기호, km, m 삭제
def _reg_sent(sent):
    # 특수기호는 빼기
    sent = re.sub(r'▶', '', sent)
    # _,_._km
    sent = re.sub(r'[0-9]{1,}\.[0-9]{1,}(km|m)', '', sent)
    return sent
    

# 한국어
def _isContainKo(text):
    ko = re.compile(r'.*[가-힇ㄱ-ㅎㅏ-ㅣ]+') 
    # return bool(ko.fullmatch(text))
    return bool(ko.match(text))  


# 한자
def _isContainKoT(text):
    kot = re.compile(r'.*[一-龥]+') 
    # return bool(ko.fullmatch(text))
    return bool(kot.match(text))   


# 영어
def _isContainEn(text):
    en = re.compile(r'.*[a-zA-Z]+') 
    # return bool(ko.fullmatch(text))
    return bool(en.match(text))  


# excel idx 
def _excel_index_creator(colum, row_idx):
    colum_idx = colum + str(row_idx)
    return colum_idx

    
# 형태소 분석
def _start_mecab(sent):
    m = Mecab()
    mor_list = m.pos(sent)
    ''' te -> list > tuple > str'''
    return mor_list


# 영어가 끝나는 인덱스 찾기 in 형태소 리스트의 
def _find_SL_idx(mor_list):
    stop_idx = 0
    for idx, mor in enumerate(mor_list):
        if mor[1] == 'SL':
            for jdx in range(idx, len(mor_list)):
                if mor_list[jdx][1] != 'SL':
                    stop_idx = jdx
                    break
    return stop_idx


# mor[_][1] 패턴 추출 및 mor[_][0] 이어서 한글 한자 영어 패턴 확인 
# mor[_][0] = 글자, mor[_][1] = 형태소
def _check_mor_dict(mor_list, stop_idx):
    each_te_dict = dict()
    kokoten = ''
    for idx in range(stop_idx):
        mor_key = mor_list[idx][1]
        kokoten += mor_list[idx][0] + ' '
        # print(mor_key)
        if mor_key not in each_te_dict:
            each_te_dict[mor_key] = 1 # 바로 더해주기
        elif mor_key in each_te_dict:
            each_te_dict[mor_key] += 1
    return kokoten


# mor_list에서 한글, 한자, 영어 추출해보기
def _extract_db_to_string(mor_list, stop_idx):
    ko, kot, en = '', '', ''

    final_mor = mor_list[0:stop_idx]
    for idx, raw in enumerate(final_mor):
        raw = final_mor[idx][0]
        mor = final_mor[idx][1]

        # 영어
        if mor == 'SL':
            # 영어가 m, km 처럼 단순히 끝나면 영어로 인식 안하고 continue
            if raw == 'm' or raw == 'km':
                continue
            en = raw # 영어는 한 덩어리로 인식

        else:
            # 한자
            if _isContainKoT(raw) == True:
                if kot == '':
                    kot = raw
                else:
                    kot += raw
            # 한글
            elif _isContainKo(raw) == True:
                if ko == '':
                    ko = raw
                else:
                    ko += raw
    
    return ko, kot, en





