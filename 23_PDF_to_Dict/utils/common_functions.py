"""
    common functions
"""

from pathlib import Path
from unicodedata import normalize
import stanza
import os
import mammoth
from konlpy.tag import Mecab
import spacy

from utils.regex_functions import *

# for spacy library
# sp = spacy.load('en_core_web_sm')


# mammoth 사용하여 docx raw test parsing
def docx_to_raw_text(file_path, stop_words):
    with open(file_path, "rb") as docx_file:
        result = mammoth.extract_raw_text(docx_file)
        text = result.value  # The raw text
        messages = result.messages  # Any messages

    contents = text.split("\n")

    contents_prep = []
    for line in contents:
        each_line = line.strip()
        if each_line and not only_char(each_line) and each_line not in stop_words and \
                not is_page_num(each_line) and not neitherKoNorEn(each_line):
            contents_prep.append(each_line)
    return contents_prep


# normalized file names
def nfd2nfc(data):
    return normalize("NFC", data)


# # Find all files in the path and subdirectories
# # {sub: [files]}
# def get_filename_dict(root, sub, ext):
#     files_dict = {}
#     print("Read files and change encoding.......\\")
#
#     path = root + sub
#     for f in Path(path).rglob(f"*{ext}"):
#         if str(f.parent) not in files_dict.keys():
#             files_dict[str(f.parent)] = [f.name]
#         else:
#             files_dict[str(f.parent)].append(f.name)
#
#     # normalize file name
#     files_dict = {nfd2nfc(k): v for k, v in files_dict.items()}
#     return files_dict


# Find all files in the path and subdirectories
# and create result directory
def get_filename_list(root, child, ext):
    files_list = []
    sub_list = []
    print("Reading " + ext + " files and change encoding.......\\")

    path = root + child + '/'
    for f in Path(path).rglob(f'*{ext}'):
        if nfd2nfc(str(f.parent)).split('/')[-1] != '작업제외':     #TM 구축시 작업제외 폴더는 skip
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


# ko 파일과 en 파일을 짝을 찾아주기 위한 함수
def file_matching(docx_ko_files, docx_en_files):
    check_matching_dict = {}

    for ko_each_file in docx_ko_files:
        change_file = change_file_name(ko_each_file)
        # 딕셔너리에 처음 등장한 경우는 1로 초기화
        if change_file[:-6] not in check_matching_dict.keys():
            # 파일이름(경로포함)에서 "한.docx" 를 제외하고 딕셔너리에 담는다
            check_matching_dict[change_file[:-6]] = 1
        else:
            # 딕셔너리에 이미 존재하는 경우 개수를 올려준다
            check_matching_dict[ko_each_file[:-6]] += 1

    for en_each_file in docx_en_files:
        change_file = change_file_name(en_each_file)
        if change_file[:-6] not in check_matching_dict.keys():
            check_matching_dict[change_file[:-6]] = 1
        else:
            check_matching_dict[change_file[:-6]] += 1

    return check_matching_dict


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
def stanza_sentence_tokenizer(text, source_language_code):
    tokenizer = stanza.Pipeline(lang=source_language_code, processors="tokenize", verbose=False)
    doc = tokenizer(text)
    return [sentence.text for sentence in doc.sentences]


# spacy tokenizer
def spacy_sentence_tokenizer(text):
    document = sp(text)
    return [sentence for sentence in document.sents]


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