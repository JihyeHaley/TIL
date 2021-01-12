"""
    common functions
"""

from pathlib import Path
from unicodedata import normalize
import stanza
import os
import mammoth
import re
from konlpy.tag import Mecab



# normalized file names
def nfd2nfc(data):
    return normalize("NFC", data)


# Find all files in the path and subdirectories
# and create result directory
def get_filename_list(root, child, ext):
    files_list = []
    sub_list = []
    print("Reading " + ext + " files and change encoding.......\\")

    path = root + child + '/'
    for f in Path(path).rglob(f'*{ext}'):
        files_list.append(str(f.parent) + '/' + f.name)
        if not str(f.parent) in sub_list:
            sub_list.append(str(f.parent))

    # normalize file name
    files_list = [nfd2nfc(f) for f in files_list]

    # create directory for result excel file
    for sub in sub_list:
        sub_dir = sub.split(child)[-1]
        if not sub_dir.strip():
            Path("./results/" + child).mkdir(parents=True, exist_ok=True)
        else:
            Path("./results/" + child + "/" + sub_dir).mkdir(parents=True, exist_ok=True)

    return files_list

# 파일이름(경로를 제외한)에서 " ", "_", "-"를 모두 "-"로 변경해주는 함수
def change_file_name(each_file):
    split_result = each_file.split("/")
    split_result[-1] = re.sub(r"( |-|_)", "-", split_result[-1])
    change_file = "/".join(split_result)
    os.rename(each_file, change_file)
    return change_file


# cache file skip function. can't be start with "~$"
def is_proper_file(file):
    temp = file.split("/")
    if temp[-1][:2] == "~$":
        return False
    return True


# 문장의 태깅 중 words_pos_list 로만 이루어져 있으면 단어들의 뭉치로 생각
def words_detect_pos(text):
    # sent_tag = ['JKO', 'EC', 'XSV', 'VV', 'EF', 'EP']
    words_pos_list = ['NNG', 'NNP', 'NNB', 'NR', 'NP', 'NNBC', 'SN', 'SY']

    pos_set = set()
    mecab = Mecab()

    ## 전체 품사 태깅
    text_pos = mecab.pos(text)

    for char in text_pos:
        pos_set.add(char[1])

    for pos in pos_set:
        if not pos in words_pos_list:
            return False

    return True


# excel idx 
def _excel_index_creator(colum, row_idx):
    colum_idx = colum + str(row_idx)
    return colum_idx



# 특수기호, km, m 삭제
def _reg_sent(sent):
    # 특수기호는 빼기
    sent = re.sub(r'▶', '', sent)
    # _,_._km
    sent = re.sub(r'[0-9]{1,}\.[0-9]{1,}(km|m)', '', sent)
    return sent