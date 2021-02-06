"""
    common functions
"""

from pathlib import Path
from unicodedata import normalize
import stanza
import os
import mammoth
from konlpy.tag import Mecab

from utils.regex_functions import *


# mammoth 사용하여 docx raw test parsing
def docx_to_raw_text(file_path, stop_words):
    with open(file_path, "rb") as docx_file:
        result = mammoth.extract_raw_text(docx_file)
        text = result.value  # The raw text
        messages = result.messages  # Any messages

    contents = text.split("\n")
    contents = text.split('。')

    return contents



# normalized file names
def nfd2nfc(data):
    return normalize("NFC", data)


# Find all files in the path and subdirectories
# {sub: [files]}
def get_filename_dict(root, sub, ext):
    files_dict = {}
    print("Read files and change encoding.......\\")

    path = root + sub
    for f in Path(path).rglob(f"*{ext}"):
        if str(f.parent) not in files_dict.keys():
            files_dict[str(f.parent)] = [f.name]
        else:
            files_dict[str(f.parent)].append(f.name)

    # normalize file name
    files_dict = {nfd2nfc(k): v for k, v in files_dict.items()}
    return files_dict


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


# TM용 문서의 종류를 가져와서 나눠준다.
# 한, 영, 병/양, non
def get_tm_doc_type(file_lists):
    ko_lists, en_lists, mix_lists, non_lists = [], [], [], []

    for each_file in file_lists:
        filename = each_file.split("/")[-1]
        if filename[-6] == "한":
            ko_lists.append(each_file)
        elif filename[-6] == "영":
            en_lists.append(each_file)
        elif filename[-6] == "병" or filename[-6] == "양":
            mix_lists.append(each_file)
        else:
            non_lists.append(each_file)

    # 한, 영, 병/양, 기타
    return (ko_lists, en_lists, mix_lists, non_lists)



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


# stanza tokenizer
def sentence_tokenizer(text, source_language_code):
    tokenizer = stanza.Pipeline(lang=source_language_code, processors="tokenize", verbose=False)
    doc = tokenizer(text)
    return [sentence.text for sentence in doc.sentences]



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
