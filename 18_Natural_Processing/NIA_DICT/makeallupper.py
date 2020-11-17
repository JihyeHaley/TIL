from mecab import *
upper = [chr(u) for u in range(65, 91, 1)] 
raw_sent = '유엔 연합 (United Nations, UN) 오쟤는 지혜 (JIHYOH)'
te, ko_words, en_words, mor_match_list_str = find_pattern_show_words(raw_sent)
# print('mor_match_list_str: ', mor_match_list_str)for j in range(len(ko_words)):
# B.  ko_word 쓰기
ko_words = ['유엔 연합', '지혜']
en_words = ['United Nations UN', 'Jihye Oh']
print(ko_words)
for j in range(len(ko_words)):
    print(ko_words[j])
    en_words= en_words[j].split(' ')
    print(en_words)
    
    if en_words[0] in upper:
        upper_cnt = 0
        final_upper_cnt  = len(en_words[j])
        for k in range(len(en_words)):
            if k in upper:
                upper_cnt += 1
        if upper_cnt == final_upper_cnt:
            print(ko_words[j])
            print(ko_words)

    # if len(ko_words) != len(mor_match_list_str):
    #     continue
    # length가 같을때는 쓰게 만들기
    print(mor_match_list_str)

