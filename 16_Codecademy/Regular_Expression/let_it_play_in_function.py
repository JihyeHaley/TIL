import re 


def get_right_ko_word(ko_words, en_words, sent):
    ko_space_ko = list()
    for idx, ko_word in enumerate(ko_words):
        first_en = en_words[idx][:2]
        # 영어 
        en_scc_and_en = f'(\({first_en})'
        # 한글 (안\붙임)
        len_first_ko = len(ko_word)
        allMatch = re.findall(en_scc_and_en, sent)
        find_this_en = allMatch[0]
        scc_en = len(find_this_en)

        # (영어 를 찾아서 어디 index부터 작업할지 찾기
        find_ko_first_index = 0
        print(f'sent: {len(sent)}')
        print(f'find_this_en: {len(find_this_en)}')
        for idx in range(0, len(sent) - scc_en):
            print(f'sent[idx:idx+scc_en]: {sent[idx:idx+scc_en]}')
            if sent[idx:idx+scc_en] == find_this_en:
                find_ko_first_index = idx
                break

        # 어디서부터 한글 탐색할지
        which_to_find_ko_index = find_ko_first_index - len(ko_word) - 4

        # 한글의 첫 글자, 한글의 마지막 글자
        ko_first, ko_last = ko_word[0], ko_word[-1]


        # 한글의 첫 글자 인덱스 default, 한글의 마지막 글자 인덱스 default
        ko_first_idx, ko_last_idx = 0, 0

        # 한글 첫 글자 찾으면 count 해줄 변수 아이
        ko_first_cnt = 0
        for index in range(which_to_find_ko_index, len(sent)):
            for idx in range(0, len(sent)):
                if sent[idx] == ko_first:
                    ko_first_idx = idx
                    ko_first_cnt += 1
                    if ko_first_cnt == 1:
                        break 
        print(f'ko_first_idx: {ko_first_idx}')
        print(sent[ko_first_idx])
        ko_made_word = ''
        for index in range(ko_first_idx, len(sent)):
            if sent[index] == ko_last:
                ko_last_idx = index
                ko_made_word = sent[ko_first_idx:ko_last_idx+1]
                print(sent[ko_first_idx:ko_last_idx+1])
                ko_space_ko.append(ko_made_word)
                break

    return ko_space_ko