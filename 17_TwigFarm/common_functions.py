'''
    common functions
'''


from pathlib import Path
from unicodedata import normalize
import stanza
import os
import mammoth

from regex_functions import *


# normalized file names
def nfd2nfc(data):
    return normalize('NFC', data)


# Find all files in the path and subdirectories
# {sub: [files]}
def get_filename_list(path, ext):
    files_dict = {}
    print('Read files and change encoding.......\\')

    for f in Path(path).rglob(f'*{ext}'):
        if str(f.parent) not in files_dict.keys():
            files_dict[str(f.parent)] = [f.name]
        else:
            files_dict[str(f.parent)].append(f.name)

    return nfd2nfc(files_dict)


# docx 파일들을 ko 파일 , en 파일 , 병합파일로 나누는 함수
def divide_files(docx_file_lists):
    ko_lists, en_lists, mix_lists = [], [], []
    for each_file in docx_file_lists:
        filename = each_file.split("/")[-1]
        if filename[-6] == "한":
            ko_lists.append(each_file)
        elif filename[-6] == "영":
            en_lists.append(each_file)
        elif filename[-6] == "병":
            mix_lists.append(each_file)
    # "..path/filename.docx" 가 영, 한, 통합 세가지로 나뉘어서 리스트에 담긴다.
    return (ko_lists, en_lists, mix_lists)



# cache file skip function. can't be start with "~$"
def is_proper_file(file):
    temp = file.split("/")
    if temp[-1][:2] == "~$":
        return False
    return True


# stanza tokenizer
def sentence_tokenizer(text, source_language_code):
    tokenizer = stanza.Pipeline(lang=source_language_code, processors='tokenize', verbose=False)
    doc = tokenizer(text)
    return [sentence.text for sentence in doc.sentences]



# 파일이름(경로를 제외한)에서 " ", "_", "-"를 모두 "-"로 변경해주는 함수
def change_file_name(each_file):
    split_result = each_file.split("/")
    split_result[-1] = re.sub(r"( |-|_)", "-", split_result[-1])
    change_file = "/".join(split_result)
    os.rename(each_file, change_file)



# mammoth 사용하여 docx raw test parsing
def docx_to_raw_text(file_path):
    with open(file_path, "rb") as docx_file:
        result = mammoth.extract_raw_text(docx_file)
        text = result.value         # The raw text
        messages = result.messages  # Any messages

    contents = text.split('\n')

    # 번호, NO/No, English, Korean, 한국어, 영어
    skip_word = ['구분', '영문', '국문', '-', '번역', '번역본', '원문', '번역요청', '원본', 'NO', '제목', '타이틀', 'Title',
                 '덕수궁관리소', '<참고>', '<영어>', '번역요청(영,일,중간,중번)', '영어:']

    contents_prep = []
    for line in contents:
        each_line = line.strip()
        if each_line and not is_meaningful(each_line) and \
                each_line not in skip_word and not is_page_num(each_line) and not neitherKoNorEn(each_line):
            contents_prep.append(each_line)
    return contents_prep

