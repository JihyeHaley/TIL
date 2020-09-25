import mammoth
import glob
import re
import os
import xlsxwriter
import timeit
import sys
from itertools import zip_longest
from pptx import Presentation
import subprocess

#ver2: Encoding 문제로 convmv로 convert 후 read
root_path = '/Users/jihyeoh/Lexcode/팀 채널 - 인공지능 학습 DB 구축 채널/1. 원본DB(렉스코드)'
sub_dir = '/4.2019한국표준협회/4.2019한국표준협회/TE-한국표준협회-ISOfocus_131_en-한'
file_path = root_path + sub_dir
print(file_path[-1])
print(file_path[:-7])
# def get_filename_list(path, ext):
#     print('Change encoding files.......\ \n')
#     result = [] 
#     for f in glob.glob(file_path + f"/*{ext}"):
#         # run convmv shell script -> file normalization NFC -> NFD (한글자소분리해결)
#         subprocess.run(['/usr/local/bin/convmv', '-f', 'utf-8', '-t', 'utf-8', '--nfc', '--notest', f])
#         result.append(f)
#     return result

# pptx_name_lists = get_filename_list(file_path, '.pptx')
# kor = 0
# en = 0
# for p in pptx_name_lists:
#     if p[-6] == '영':
#         kor += 1
#     else:
#         en += 1
# print(f'kor : {kor}, en: {en}')