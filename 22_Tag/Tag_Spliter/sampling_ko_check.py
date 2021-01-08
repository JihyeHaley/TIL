import pandas as pd
import random
import xlsxwriter 
import os


ko_ja_list = list()
ko_ja_check = list()
ko_ja_duplicate = dict()
with open('./ko/ko_ja_choice_idx.txt', 'r') as ko_ja_no:
    ko_ja_list = ko_ja_no.readlines()

for _ in range(len(ko_ja_list)):
    if ko_ja_list[_] not in ko_ja_check:
        ko_ja_check.append(ko_ja_list[_])
    elif ko_ja_list[_] in ko_ja_check:
        ko_ja_duplicate[_] = ko_ja_list[_]


print(f'ko_ja_check: {len(ko_ja_check)}')
print(f'ko_ja_duplicate: {len(ko_ja_duplicate)}')

completed_ko_ja_duplicated = open(f'./ko_ja_duplicated'+ '.txt', "w+")
for key in ko_ja_duplicate.keys():
    completed_ko_ja_duplicated.write(str(key)+'\n')
completed_ko_ja_duplicated.close()

completed_ko_ja_unduplicated = open(f'./ko_ja_unduplicated'+ '.txt', "w+")
for key in ko_ja_check:
    completed_ko_ja_unduplicated.write(str(key))
completed_ko_ja_unduplicated.close()




