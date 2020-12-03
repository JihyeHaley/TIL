
"""
    sentence_splitter
    split_sentence('/path/to/사회과학_test')
"""

import os
import logging
import argparse
import pandas as pd
from tqdm import tqdm
from pathlib import Path
from unicodedata import normalize
from nltk.tokenize import sent_tokenize
import re


parser = argparse.ArgumentParser(description=__doc__)
# set the argument formats
parser.add_argument('--path', '-p', default='./results/', help='parent dir')

#logging.basicConfig(format='%(levelname)s - %(asctime)s :: %(message)s', level=logging.INFO)

def split_sentence(input_path, rule_path):

    # Open log files: record the order of file names
    completed_log = open(f'./results/'+ input_path.split('/')[0] + '/00_' + input_path.split('/')[-1] + '_split_ERROR_LOG.txt', "w+")

    # Define tm's index start number :: index format == f'{root dir name}_{number}'
    global index_start
    index_start = 0

    # Find index of 50th character except white space.
    def _find_index(st):
        cnt = 0
        index = 0
        for char in st:
            index += 1
            if char != ' ':
                cnt += 1
                if cnt == 50:
                    return index
        return index

    # 문장의 끝이 [인용. 참조. 단. 숫자. 알파벳. 쪽. ).] 은 번역필요에서 제외
    def non_sentence_end(text):
        sent_end_regex = re.compile(r'(((인용)|(참조)|단|\d|[a-zA-Z]|쪽|\))\.)$')
        return bool(sent_end_regex.search(text))


    # Find tm which have less than 50 characters except white space.
    def find_short(tm, find_target=False):
        if type(tm) != str:
            return None
        tm = tm.strip()
        idx = _find_index(tm)
        see = tm[idx:]    # In a string after 50th characters, if it has white space less than one, it is included in short sentences.

        # 문장의 끝이 [?, !, 다, 음, 임, 됨, 함] + [.]으로 끝나는문장 중 제외되는 단어들 빼고 번역필요로 인식
        if tm and (tm[-1] in ['?', '!', '다', '음', '임', '됨', '함'] or (tm[-1] == '.' and len(tm) > 1 and not non_sentence_end(tm))) and see.count(' ') < 2:
            if find_target:
                return '번역필요'    # If find_target==True, the tm is classified as a translation target.
            return tm

    # Find tm which have more than 50 characters except withe space
    def find_long(tm):
        if type(tm) != str:
            return None
        idx = _find_index(tm)
        see = tm[idx:]
        if see and see.count(' ') >= 2:
            return tm

    def _size(t):
        if type(t) == list:
            return len(t)
        return 0

    # Each element contained in the list should be assigned to one cell without disordering.
    def _flatten(df):
        original_final, modified_final = [], []
        for idx in range(len(df)):
            line = df.iloc[idx]      # Extract one line(row) in dataframe.
            original_temp, modified_temp = [line['original']], [line['modified']]
            if line['size'] != 0:    # 'modified' data can be list or str. if 'modified' is a list,the code below will be progressed
                original_temp.extend(['' for _ in range(line['size'] - 1)])
                modified_temp = line['modified']
            original_final.extend(original_temp)
            modified_final.extend(modified_temp)
        return original_final, modified_final

    # split sentences
    def _split_sentence(tm, idx=0):
        """
        type(Input) == str
        type(Output) == list
        """
        if idx == len(rules):    # 마지막 룰이 적용되었을 때 str 반환
            return tm
        rule = rule_lookup.iloc[idx]
        rule_result = rule_result_lookup.iloc[idx]
        st = tm.split(rule)

        # remove start with , and strip the sentence
        st = [_st[1:].strip() if _st and _st.strip()[0] == ',' else _st.strip() for _st in st]

        temp_list = sent_tokenize(rule_result)
        for i in range(1, len(st)):
            if len(temp_list) > 2:
                logging.warning('한 문장은 세개 이상으로 쪼개질 수 없습니다.')
                continue
            elif len(temp_list) == 2:
                st[i] = temp_list[1] + st[i]
            st[i - 1] += temp_list[0]
        idx += 1
        return [_split_sentence(i, idx) for i in st]


    # tm's index format == f'{root dir name}_{number}'
    def _make_tm_index(path, index_num):
        # name = path.split('/')[1]
        name = path.split('/')[2]
        return f'{name}_{index_num}'


    def process(data, path):
        global index_start

        short = data.map(lambda x: find_short(x)).dropna()
        long = data.map(lambda x: find_long(x)).dropna()

        if not len(long):
            original_final = data.tolist()
            modified_final = data.tolist()
        else:
            sent_split = long.map(lambda x: eval(str(f'[{str(_split_sentence(x)).replace("[", "").replace("]", "")}]')))
            # _split_sentence(x)의 리턴값은 다중 리스트로 나오고, 위의 과정을 이용해서 flat한 리스트로 바꿔줍니다.
            ser_processed = pd.concat([sent_split, short]).sort_index()
            tm = pd.DataFrame({'original': data, 'modified': ser_processed}).dropna()
            tm['size'] = tm.modified.map(lambda x: _size(x))
            original_final, modified_final = _flatten(tm)

        ori_trans_or_not = pd.Series(map(lambda x: find_short(x, find_target=True), original_final))
        mod_trans_or_not = pd.Series(map(lambda x: find_short(x, find_target=True), modified_final))

        # Count the number of characters without white space.
        ori_char_len = pd.Series(map(lambda x: len(x) - x.count(' '), original_final))
        mod_char_len = pd.Series(map(lambda x: len(x) - x.count(' '), modified_final))

        file_len = len(modified_final)
        index_final = index_start+file_len
        index = pd.Series(map(lambda num: _make_tm_index(path, num), range(index_start, index_final)))    # make tm's index
        index_start = index_final    # Update the index_start
        path_col = pd.Series(map(lambda x: path, range(file_len)))    # Make file path column.
        fin = pd.DataFrame({'ID': index, '경로': path_col,
                            '국문_원문': original_final, '국문_수정': modified_final,
                            # '글자수_원문': ori_char_len, '번역여부_원문': ori_trans_or_not,
                            '글자수': mod_char_len, '번역여부': mod_trans_or_not}) #.set_index(index)
        # set index name
        # fin.index.names = ['ID']
        return fin, file_len

    # Call rules and prepare to use.
    cat = pd.read_excel(rule_path)
    rules = cat[cat['대상'] == 'Y']
    rule_lookup = rules['유형']
    rule_result_lookup = rules['나누기']

    # Prepare output directory
    p = Path(input_path)
    output_root = f'{p.parent}/{p.name}_split'
    if not os.path.isdir(output_root):
        os.mkdir(output_root)

    # Call target files
    total = []
    for f in tqdm(Path(input_path).rglob(f'*.xlsx')):
        file_path = str(f.parent) + '/' + f.name
        file_name = f'{file_path.split("/")[-1][:-5]}_split'
        output_path = f'{output_root}/{"/".join(file_path.split("/")[2:-1])}_split'
        Path(output_path).mkdir(parents=True, exist_ok=True)
        try:
            raw_data = pd.read_excel(file_path)
        except Exception as e:
            #logging.warning(f'[FILE READ ERROR] - {file_path}')
            completed_log.write(f'[FILE READ ERROR] - {file_path} \n')
            continue
        if not len(raw_data):
            #logging.warning(f'[EMPTY FILE] - {file_path}')
            completed_log.write(f'[EMPTY FILE] - {file_path} \n')
            continue
        ko = raw_data['KOR']
        path = raw_data['FILE'].iloc[0]
        fin, file_len = process(ko, path)
        fin.to_excel(f'{output_path}/{file_name}_{file_len}.xlsx')
        total.append(fin)

    for_inspect = pd.concat(total)

    # 수정된 글자수 80자 이하로만 뽑기
    for_inspect = for_inspect[for_inspect['글자수'] < 81]

    # NO column 추가
    num_cols = [i for i in range(1, len(for_inspect) + 1)]
    for_inspect['NO'] = num_cols
    for_inspect = for_inspect[['NO', 'ID', '경로', '국문_원문', '국문_수정', '글자수', '번역여부']]
    # for_inspect.to_excel(f'{output_root}/for_inspect_total.xlsx')
    for_inspect.to_excel(f'{output_root}/{input_path.split("/")[-1].strip()}_split_total_{len(for_inspect)}.xlsx', index=False)


if __name__ == '__main__':
    # split_sentence(input_path='../data/testtest', rule_path='../data/유형정리.xlsx')
    #split_sentence(input_path='/Users/hyeonakim/Desktop/root_dir', rule_path='./data/유형정리.xlsx')

    args = parser.parse_args()

    # args.path: include '/'
    #path = args.path + 'run'
    path = args.path + '예체능'

    parent_dir = sorted([f.name for f in os.scandir(path) if f.is_dir()])
    parent_dir = [normalize("NFC", f) for f in parent_dir]

    for sub_dir in parent_dir:
        print('Reading :', sub_dir)
        #split_sentence(input_path='./results/사회과학/' + sub_dir, rule_path='./data/유형정리.xlsx')
        #split_sentence(input_path='./results/공학/' + sub_dir, rule_path='./data/유형정리.xlsx')
        split_sentence(input_path=path + '/' + sub_dir, rule_path='./data/유형정리.xlsx')
        print('Done! \n')