import os
import glob
import argparse
from datetime import datetime
from collections import Counter
from utils.data_cleaner import *
import logging


parser = argparse.ArgumentParser(description='Crawl specific domain')

parser.add_argument('--input', '-i',
                    type=str,
                    help='<type: str> input file path')
parser.add_argument('--is_from_web', '-w',
                    type=bool,
                    default=True)
parser.add_argument('--is_dir', '-d',
                    type=bool,
                    default=False)
parser.add_argument('--output', '-o',
                    type=str,
                    default='../data/')
parser.add_argument('--keyword', '-n',
                    type=str)
parser.add_argument('--ko_col_name', '-k',
                    type=str,
                    default='ko-kr')
parser.add_argument('--target_col_name', '-t',
                    type=str,
                    default='en-us')
parser.add_argument('--loglevel', '-v',
                    default='debug')
args = parser.parse_args()
input_path = args.input
output_path = args.output
is_from_web = args.is_from_web
is_dir = args.is_dir
ko = args.ko_col_name
target = args.target_col_name
log_level = args.loglevel

KEYWORD = args.keyword
KOREAN = re.compile(r'[가-힣]+')
NO_KOREAN = re.compile(r'^[^가-힣]*$')
NOW = datetime.now().strftime('%Y%m%d_%H%M%S')
KO_SPECIAL_CHAR = re.compile(r"[^ㄱ-ㅎㅏ-ㅣ가-힣a-zA-Z0-9\s,:'%$₩~—–-]")
EN_SPECIAL_CHAR = re.compile(r"[^a-zA-Z0-9\s,:'%$₩~—–-]")

file_ext = input_path.split('.')[-1]

if file_ext not in ['csv', 'xlsx'] and is_dir:
    assert True
elif file_ext in ['csv', 'xlsx'] and not is_dir:
    assert True

level_lookup = {'debug': logging.DEBUG,
                'info': logging.INFO,
                'warning': logging.WARNING,
                'error': logging.ERROR,
                'critical': logging.CRITICAL}
levels = list(level_lookup.keys())
assert log_level in levels, f'You can choose log level in {levels}'
LOG_LEVEL = level_lookup[log_level]
LOG_FORMAT = '%(levelname)s - %(asctime)s :: %(message)s'

logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)

def preprocess(file, output_path):
    if file.split('.')[-1] == 'csv':
        raw_data = pd.read_csv(file)
    elif file.split('.')[-1] == 'xlsx':
        raw_data = pd.read_excel(file)

    data, url_col, keys = pick_cols(raw_data, [ko, target])

    data, ko_only = separate_loner(data, ko)
    data, target_only = separate_loner(data, target)
    logger.info('하나의 셀에 하나의 데이터 할당 중')
    if is_from_web:
        data = flatten(data)
    logger.info('유효하지 않은 데이터 제거 중')
    a_df = rmv_ugly(data, ko, NO_KOREAN)
    b_df = rmv_ugly(a_df, target, KOREAN)
    units = b_df.fillna('NoneFlag') # rmv_single_words(b_df, ko).fillna('NoneFlag')
    logger.info('구두점 체크 중')
    if target in ['en', 'en-us']:
        units[target] = units[target].map(lambda x: capitalize(x))
    tm = unify_quotes(units)
    ko_specials = tm[ko].map(lambda x: Counter(re.findall(KO_SPECIAL_CHAR, x)))
    target_specials = tm[target].map(lambda x: Counter(re.findall(EN_SPECIAL_CHAR, x)))
    tm['ko_period'] = ko_specials.map(lambda x: x['.'])
    tm['target_period'] = target_specials.map(lambda x: x['.'])
    tm['ko_qmark'] = ko_specials.map(lambda x: x['?'])
    tm['target_qmark'] = target_specials.map(lambda x: x['?'])
    logger.info('하나의 셀에 하나의 문장 할당 중')
    ko_doc, target_doc, index2drop, urls = [], [], [], []
    for i in tm.index:
        tu = tm.loc[i, :]
        if (tu['ko_period'] + tu['ko_qmark']) > 1 or (tu['target_period'] + tu['target_qmark']) > 1:
            index2drop.append(i)
            ko_sents = tokenize_sentence(tu[ko], ko)
            target_sents = tokenize_sentence(tu[target], target)
            ko_l = len(ko_sents)
            tar_l = len(target_sents)
            if url_col:
                urls.extend([tu['url'] for i in range(max(ko_l, tar_l))])
            if ko_l > tar_l:
                target_sents += ['NoneFlag' for i in range(ko_l - tar_l)]
            elif ko_l < tar_l:
                ko_sents += ['NoneFlag' for i in range(tar_l - ko_l)]
            ko_doc += ko_sents
            target_doc += target_sents
    tm = tm.drop(index2drop)
    if url_col:
        temp = {
                ko: ko_doc,
                target: target_doc,
                'url': urls,
                'ko_period': [sentence.count('.') for sentence in ko_doc],
                'target_period': [sentence.count('.') for sentence in target_doc],
                'ko_qmark': [sentence.count('?') for sentence in ko_doc],
                'target_qmark': [sentence.count('?') for sentence in target_doc],
                }
    else:
        temp = {
                ko: ko_doc,
                target: target_doc,
                'ko_period': [sentence.count('.') for sentence in ko_doc],
                'target_period': [sentence.count('.') for sentence in target_doc],
                'ko_qmark': [sentence.count('?') for sentence in ko_doc],
                'target_qmark': [sentence.count('?') for sentence in target_doc],
                }

    final_tm = pd.concat([tm, pd.DataFrame(temp)]).drop_duplicates(subset=[ko, target])
    # logger.info('비어 있는 셀 표시 중')
    # workbook = highlight_none(final_tm)
    output_name = f'{output_path}END_{file.split("/")[-1][:-4]}.xlsx'
    # workbook.save(filename=output_name)
    # logger.info(f'엑셀 파일로 저장 완료 :: 다음의 경로를 확인하세요. {output_name}')
    final_tm.to_excel(output_name, index=False)


if is_dir:
    output_dir = f'{output_path}RESULT_{NOW}/'
    os.mkdir(output_dir)
    csv_files = glob.glob(os.path.abspath((f'{input_path}{KEYWORD}*.csv')))
    xlsx_files = glob.glob(os.path.abspath((f'{input_path}{KEYWORD}*.xlsx')))
    for file in csv_files+xlsx_files:
        preprocess(file, output_dir)
else:
    preprocess(input_path, output_path)
