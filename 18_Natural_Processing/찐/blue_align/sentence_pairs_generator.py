import pandas as pd
import argparse
import os
import sys

from utils.google_api import google_translate
from utils.parser_api import parse_file
from bleualign.align import Aligner

GOOGLE_SPLIT_SIZE = 100


def write_cells(sources, targets, source_lang, target_lang):
    df = pd.DataFrame(columns=[source_lang, target_lang])

    for i, (src, tgt) in enumerate(zip(sources, targets)):
        if src != '' or tgt != '':
            df.loc[i + 1, source_lang] = src
            df.loc[i + 1, target_lang] = tgt

    df.to_excel('data/test/sentence_pairs_result.xlsx', engine='xlsxwriter')


def make_google_reference_list(source_list, source_lang, target_lang):
    reference_list = []
    src_text_size = len(source_list)
    src_text_slice_count = src_text_size // GOOGLE_SPLIT_SIZE + 1
    for i in range(src_text_slice_count):
        start_pos = i * GOOGLE_SPLIT_SIZE
        end_pos = start_pos + GOOGLE_SPLIT_SIZE
        if end_pos > src_text_size:
            sub_list = source_list[start_pos:]
        else:
            sub_list = source_list[start_pos:end_pos]

        df = pd.DataFrame(sub_list)
        df = df.drop_duplicates()
        translated = google_translate('\n'.join(df[0].tolist()), source_lang, target_lang)
        translated_list = [translated[sentence] for sentence in sub_list]
        reference_list.extend(translated_list)

    return reference_list


def align_sentences(source_list, target_list, reference_list):
    aligner = Aligner(None)
    aligner.multialign = aligner.get_align(source_list, target_list, reference_list, [])
    return aligner.get_mainloop(source_list, target_list, reference_list, [])


def generate_pairs(source_lang, target_lang, source_file, target_file, srctotarget_file, is_reference_save):

    source_sentences = parse_file(source_file, source_lang)
    target_sentences = parse_file(target_file, target_lang)

    source_list = [value['text'] for value in source_sentences['sentences'] if value['text']]
    target_list = [value['text'] for value in target_sentences['sentences'] if value['text']]

    if srctotarget_file:
        with open(srctotarget_file, 'r') as srctotarget:
            reference_list = srctotarget.readlines()
            refs = [reference_list]
    else:
        reference_list = make_google_reference_list(source_list, source_lang, target_lang)
        reference_list = [string + '\n' for string in reference_list]
        refs = [reference_list]

        if is_reference_save:
            with open('test_data/misc_test/ref.txt', 'w') as reference_file:
                for sentence in reference_list:
                    reference_file.write(sentence)

    sources, targets = align_sentences(source_list, target_list, refs)
    return sources, targets


def parse_args(argv):
    """Parse command line arguments.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    # set the argument formats
    parser.add_argument(
        '--source_lang', '-src_lang', default='ko',
        help='source language')
    parser.add_argument(
        '--target_lang', '-tgt_lang', default='en',
        help='target language')
    parser.add_argument(
        '--source_file', '-src_file', default=os.path.join('data', 'test', 'TE-한국표준협회-222호_CES technology trends for 2018-영한A.docx'),
        help='source file')
    parser.add_argument(
        '--target_file', '-tgt_file', default=os.path.join('data', 'test', 'TE-한국표준협회-222호_CES technology trends for 2018-영한B.docx'),
        help='target file')
    parser.add_argument(
        '--source_to_target_file', '-srctotgt_file', default=os.path.join('data', 'test', 'ref.txt'),
        help='source to target file')
    parser.add_argument(
        '--is_reference_save', '-ref', default=False,
        help='whether you want to save the reference file or not')

    return parser.parse_args(argv[1:])


if __name__ == '__main__':
    args = parse_args(sys.argv)
    sources, targets = generate_pairs(args.source_lang, args.target_lang, args.source_file, args.target_file, None, args.is_reference_save)
    write_cells(sources, targets, args.source_lang, args.target_lang)
