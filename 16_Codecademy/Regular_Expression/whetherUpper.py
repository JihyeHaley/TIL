
lower = [chr(l) for l in range(97, 123, 1)]
upper = [chr(u) for u in range(65, 91, 1)] 

ko_word = [['순환종양세포'], ['오지혜']]
en_word = [['CTC ', 'circulating', 'tumor' 'cell'], ['Jihye Oh']]

ko_word_out_index = 0

for e in range(len(en_word)):
    print(en_word[e])
    for idx in range(len(en_word[e])):
        i = en_word[e][idx].strip(' ')
        print(i)
        i_len = len(i)
        print(i_len)
        i_cnt = 0
        # 대문자 개수 
        for _ in range(i_len):
            if i[_] in upper:
                print(i[_])
                i_cnt += 1
            print(i_cnt)
        if i_cnt == i_len:
            print('일치했다')
            i = en_word[e].pop(idx)
            ko_word.append(ko_word[ko_word_out_index])
            en_word.append([i])
            break
        else:
            ko_word_out_index += 1
            continue
            
    
print(ko_word)
print(en_word)



# 대문자인 것들만 있는게 있는지 확인하기
def isAllUpper(en_words):
    upper = [chr(u) for u in range(65, 91, 1)] 

    upper_cnt = 0
    for en_word  in en_words:
        for _ in en_word:
            if _ in upper:
                upper_cnt += 1
        if upper_cnt == len(en_word):
            return True
        else:
            return False


# 대문자로된 약자만 추출
def check_all_upper(ko_words, en_words):
    upper = [chr(u) for u in range(65, 91, 1)] 
    ko_word_out_index = 0

    for e in range(len(ko_words)):
        print(en_words[e])
        for idx in range(len(en_words[e])):
            i = en_words[e][idx].strip(' ')
            print(i)
            i_len = len(i)
            print(i_len)
            i_cnt = 0
            # 대문자 개수 
            for _ in range(i_len):
                if i[_] in upper:
                    print(i[_])
                    i_cnt += 1
                print(i_cnt)
            if i_cnt == i_len:
                print('일치했다')
                i = en_words[e].pop(idx)
                ko_words.append(ko_words[ko_word_out_index])
                en_words.append([i])
                break
            else:
                ko_word_out_index += 1
                continue

    return ko_words, en_words