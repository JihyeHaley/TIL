import nltk

from tensorflow.keras.preprocessing.text import text_to_word_sequence

# A - 1. 형태소 분석 nltk tokenizer
def _work_start_tokenizer(sent):
    # 단어만 남기기
    pre_words_list = text_to_word_sequence(sent) # [Hi, My, name, is, jihye] (문장의 첫 단어도 )
    
    # tensflow는 마침표는 가져오지 않는다. 따라서, nlt tokenize로 가장 마지막 맞침표만 챙겨온다.
    pre_words_list_1 = nltk.tokenize.word_tokenize(sent)[-1] # 마지막 마침표 ... 떨어뜨려주기
    if pre_words_list_1 in [',', '.', '!', '?']:
        pre_words_list.append(pre_words_list_1)
    
    words_list = list()
    for word in pre_words_list:
        pre = word.split(' ')
        for _ in pre:
            words_list.append(_)

    # 단어와 형태소 List
    words_mor_list = nltk.tag.pos_tag(words_list) # [(Hi, NNG), ...] 

    # 형태소만 
    mor_list = list()
    for each_mor in words_mor_list:
        mor_list.append(each_mor[1]) # [NNG, NNP, VB ...]

    return words_list, mor_list, words_mor_list


# A- 2. (작업용) 단어 바꿔주기 
def _work_connet_change(tp, idx, words_list, mor_list, words_mor_list):
    if tp == 'vbin':
        words_list[idx] = f'{words_mor_list[idx][0]} {words_mor_list[idx+1][0]}' # 동사 두개 이어줌!
        mor_list[idx] = f'{words_mor_list[idx][1]} {words_mor_list[idx+1][1]}' # 형태소 두개 이어줌!
        words_list.pop(idx+1) # 뒤에 단어는 삭제해주기
        mor_list.pop(idx+1) # 뒤에 형태소는 삭제해주기
    return words_list, mor_list


# A - 3. (조건용) 동사 전치사 이어주기 # [(Hi, NNG), ...] = [(단어, 형태소), ...]
def _work_vb_in_connect(words_list, mor_list, words_mor_list):
    for idx, each_word_mor in enumerate(words_mor_list):
        if each_word_mor[1] == 'VB' or each_word_mor[1] == 'NN':
            if idx == len(words_mor_list) - 1: # 끝번호면 작업하면 index error
                continue
            else: # 앞에 관사('DT')가 없으면 명사('NN')로 인식해서 가져가시오
                if words_mor_list[idx-1][1] != 'DT' and words_mor_list[idx+1][1] == 'IN' and words_mor_list[idx+2][1] != 'FW' and words_mor_list[idx-1][1] != 'IN': 
                    words_list, mor_list = _work_connet_change('vbin', idx, words_list, mor_list, words_mor_list)
    return words_list, mor_list


# C - 4. <b> 를 slicing 해서 더해주기
def _work_add_and_completed(sent, words_list, diff_idx):
    word_diff = str()

    if diff_idx == 0:
        first_letter = sent.split(' ')[0][0] # 첫 단 대문자 처리 
        word_diff = f'<b>{first_letter}{words_list[diff_idx][1:]}</b>'
    else:
        word_diff = f'<b>{words_list[diff_idx]}</b>'
    
    words_list[diff_idx] = word_diff
    
    return words_list 


# C - 5. 띄어쓰기 신경써서 문장 만들어주기
def _work_connect_word(a_words, b_words, c_words, a, b, c):
    pre_output_result_list = list()
    a_completed, b_completed, c_completed = str(), str(), str()

    for jdx in range(len(a_words)):
        if jdx == 0:
            if a_words[jdx] != b_words[jdx] or b_words[jdx] != c_words[jdx] or a_words[jdx] != c_words[jdx]:
                a_completed += a_words[jdx]
                b_completed += b_words[jdx]
                c_completed += c_words[jdx]
                
            else: 
                a_completed += f'{a[0]}{a_words[jdx][1:]}'
                b_completed += f'{b[0]}{b_words[jdx][1:]}'
                c_completed += f'{c[0]}{c_words[jdx][1:]}'
                

        # 마지막 인덱스는 띄어 쓰기 없이 만나기
        elif jdx == len(a_words) - 1:
            a_completed += a_words[jdx]
            b_completed += b_words[jdx]
            c_completed += c_words[jdx]

        else:
            # 띄어쓰기
            a_completed += ' ' + a_words[jdx]
            b_completed += ' ' + b_words[jdx]
            c_completed += ' ' + c_words[jdx]
    
    pre_output_result_list = a_completed, b_completed, c_completed
    
    return pre_output_result_list