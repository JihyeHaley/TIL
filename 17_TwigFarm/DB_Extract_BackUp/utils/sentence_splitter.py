"""
    sentence_splitter
    split_sentence('/path/to/사회과학_test')
"""

import pandas as pd
import kss
import re
from tqdm import tqdm
import os
import stanza


from pathlib import Path
import logging


logging.basicConfig(format='%(levelname)s - %(asctime)s :: %(message)s', level=logging.INFO)

def split_sentence(input_path, rule_path):

    global index_start
    index_start = 0

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

    def find_short(tm, find_target=False):
        if type(tm) != str:
            return None
        tm = tm.strip()
        idx = _find_index(tm)
        see = tm[idx:]
        if tm and tm[-1] in ['.', '?', '!', '다', '음', '임'] and see.count(' ') < 2:
            if find_target:
                return '번역필요'
            return tm

    def find_long(tm):
        if type(tm) != str:
            return None
        idx = _find_index(tm)
        see = tm[idx:]
        if see and see.count(' ') >= 2:
            return tm

    def _sub(sentence, rule):
        labels = []
        for key in rule.keys():
            exist = re.search(key, sentence)
            if exist:
                labels.append(exist.span()[0])
            else:
                continue
            sentence = re.sub(key, rule[key], sentence)
        return str(labels), sentence

    def _size(t):
        if type(t) == list:
            return len(t)
        return 0

    def _flatten(df):
        original_final, modified_final = [], []
        for idx in range(len(df)):
            line = df.iloc[idx]
            original_temp, modified_temp = [line['original']], [line['modified']]
            if line['size'] != 0:
                original_temp.extend(['' for _ in range(line['size'] - 1)])
                modified_temp = line['modified']
            original_final.extend(original_temp)
            modified_final.extend(modified_temp)
        return original_final, modified_final

    def _split_sentences(tm, tokenizer_name='kss'):
        end_sent_regex = re.compile(r'(다\.)')
        if tokenizer_name == 'kss':
            temp_list = kss.split_sentences(tm)
            return [re.sub(end_sent_regex, r'\1 ', x) for x in temp_list]
        elif tokenizer_name == 'stanza':
            stanza.download('ko', logging_level='WARN')
            tokenizer = stanza.Pipeline(lang='ko', processors='tokenize')
            doc = tokenizer(tm)
            return [re.sub(end_sent_regex, r'\1 ', sentence.text) for sentence in doc.sentences]

    def _make_index(path, index_num):
        for name in path.split('/'):
            if name != '':
                return f'{name}_{index_num}'

    def process(data, path):
        global index_start

        short = data.map(lambda x: find_short(x)).dropna()
        long = data.map(lambda x: find_long(x)).dropna()

        if not len(long):
            original_final = data.tolist()
            modified_final = data.tolist()
        else:
            modified = long.map(lambda x: _sub(x, rule))
            A = modified.tolist()
            index, sentences = list(map(list, zip(*A)))
            df_split = pd.DataFrame({'original': long, 'modified': sentences, 'index': index})
            onemore = df_split[df_split['index'] != '[]']
            _long = long.drop(onemore.index)
            sent_toked = onemore['modified'].map(lambda text: _split_sentences(text))
            ser_processed = pd.concat([_long, sent_toked, short]).sort_index()
            tm = pd.concat([data, ser_processed], axis=1).dropna().rename(columns={'KOR': 'original', 0: 'modified'})
            tm['size'] = tm.modified.map(lambda x: _size(x))
            original_final, modified_final = _flatten(tm)

        ori_trans_or_not = pd.Series(map(lambda x: find_short(x, find_target=True), original_final))
        mod_trans_or_not = pd.Series(map(lambda x: find_short(x, find_target=True), modified_final))
        ori_char_len = pd.Series(map(lambda x: len(x) - x.count(' '), original_final))
        mod_char_len = pd.Series(map(lambda x: len(x) - x.count(' '), modified_final))
        file_len = len(modified_final)
        index_final = index_start+file_len
        index = pd.Series(map(lambda num: _make_index(path, num), range(index_start, index_final)))
        index_start = index_final
        path_col = pd.Series(map(lambda x: path, range(file_len)))
        # path_col = [path for _ in range(file_len)]
        fin = pd.DataFrame({'경로': path_col,
                            '국문 원문': original_final, '국문 수정': modified_final,
                            '글자수_ori': ori_char_len, '번역여부_ori': ori_trans_or_not,
                            '글자수_mod': mod_char_len, '번역여부_mod': mod_trans_or_not}).set_index(index)
        return fin, file_len

    # 적용할 바꿀 규칙 호출 후 준비
    cat = pd.read_excel(rule_path)

    rules = cat[cat['대상'] == 'Y']
    df = pd.concat([rules['유형'], rules['나누기']], axis=1)
    rule = {}
    for i in range(len(df)):
        row = df.iloc[i]
        rule[row['유형']] = row['나누기']
    keys = rule.keys()
    for key in keys:    # 괄호가 포함된 rule일 경우 에러를 유발하므로 raw text로 변환시켜준다.
        if key.count(')') or key.count('('):
            _val = r'{}'.format(rule[key]).replace(r')', r'\)').replace(r'(', r'\(')
            _key = r'{}'.format(key).replace(r')', r'\)').replace(r'(', r'\(')
            del rule[key]
            rule[_key] = _val
            break


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
            logging.warning(f'아래 경로의 파일을 읽던 중 문제가 발생했습니다. 파일이 정상인지 확인하세요.\n\t\t\t{file_path}')
            continue
        if not len(raw_data):
            logging.warning(f'아래 경로의 파일에 유효한 데이터가 없습니다. 원본 파일을 확인하세요.\n\t\t\t{file_path}')
            continue
        ko = raw_data['KOR']
        path = raw_data['FILE'].iloc[0]
        fin, file_len = process(ko, path)
        fin.to_excel(f'{output_path}/{file_name}_{file_len}.xlsx')
        total.append(fin)
    for_inspect = pd.concat(total)
    # for_inspect.to_excel(f'{output_root}/for_inspect_total.xlsx')
    for_inspect.to_excel(f'{output_root}/{input_path.split("/")[-1].strip()}_for_inspect_total.xlsx')


if __name__ == '__main__':
    split_sentence(input_path='../data/testtest', rule_path='../data/유형정리.xlsx')
    # split_sentence(input_path='./results/사회과학/)', rule_path='./data/유형정리.xlsx')

