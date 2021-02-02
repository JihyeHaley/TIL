import os
import re

from pathlib import Path
from unicodedata import normalize

from utils.regex_functions import *


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




