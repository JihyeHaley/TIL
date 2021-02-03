# a. search_length
def _find_search_length(g_w, p_w):
    search_length = int()
    if len(g_w) > len(p_w):
        search_length = len(p_w)
    elif len(g_w) < len(p_w):
        search_length = len(g_w)
    elif len(g_w) == len(p_w):
        search_length = len(g_w) + 1

    return search_length


# b. first_idx
def _find_first_idx(g_w, p_w, search_length):
    first_idx = str()
    for idx in range(search_length):
        if g_w[idx] != p_w[idx]:
            if idx == 0:
                if g_w[idx+1] == p_w[idx]:
                    first_idx = 'front_gg_more_' + str(idx)
                elif g_w[idx] == p_w[idx+1]:
                    first_idx = 'front_ppg_more_' + str(idx)
                else:
                    first_idx = str(idx)
            elif idx >= 1:
                first_idx = str(idx)
            break

    return first_idx


# c. last_idx
def _find_last_idx(g_w, p_w, search_length):
    last_idx = str()
    for jdx in range(1, search_length):
        print(-jdx)
        if jdx == 1:
            if g_w[-jdx-1] == p_w[-jdx]:
                    last_idx = 'back_gg_more_' + str(jdx)
            elif g_w[-jdx] == p_w[-jdx-1]:
                last_idx = 'back_ppg_more_' + str(jdx)
            else:
                if g_w[-1] != p_w[-1]:
                    last_idx = str(-1)
                    break
        else:
            if g_w[-jdx] != p_w[-jdx]:
                last_idx = str(-jdx + 1)
                break 

    return last_idx

# d. <b>, </b>
def _add_b_tag(g_w, p_w, first_idx, last_idx):
    print(first_idx, last_idx)
    if 'front_gg_more_' in first_idx:
        first_idx = int(first_idx.strip('front_gg_more_')) # became number
        if first_idx == 0:
            g_w[0] = f'<b>{g_w[0]}'
            g_w[1] = f'{g_w[1]}</b>'
            p_w[0] = f'<b>{p_w[0].capitalize()}</b>'
    elif 'front_ppg_more_' in first_idx:
        first_idx = int(first_idx.strip('front_ppg_more_')) # became number
        if first_idx == 0:
            p_w[0] = f'<b>{p_w[0]}'
            p_w[1] = f'{p_w[1]}</b>'
            g_w[0] = f'<b>{g_w[0].capitalize()}</b>'
    else:
        if 'back_gg_more_' in last_idx:
            last_idx = int(last_idx.strip('back_gg_more')) # became number
            if last_idx == 1:
                g_w[-1] = f'<b>{g_w[-1]}'
                g_w[-2] = f'{g_w[-2]}</b>'
                p_w[-1] = f'<b>{p_w[-1]}</b>'
        elif 'back_ppg_more_' in last_idx:
            last_idx = int(last_idx.strip('back_ppg_more_')) # became number
            if last_idx == 1:
                p_w[-1] = f'<b>{p_w[-1]}'
                p_w[-2] = f'{p_w[-2]}</b>'
                g_w[-1] = f'<b>{g_w[-1]}</b>'
        else:
            if first_idx == '' or last_idx == '':
                if first_idx == '':
                    last_idx = int(last_idx)
                    g_w[last_idx] = f'<b>{g_w[last_idx]}</b>'
                    p_w[last_idx] = f'<b>{p_w[last_idx]}</b>'
               
            else:
                first_idx = int(first_idx) # became number
                last_idx = int(last_idx)
                if first_idx == 0:
                    g_w[first_idx] = f'<b>{g_w[first_idx].capitalize()}'
                    p_w[first_idx] = f'<b>{p_w[first_idx].capitalize()}'
                else:
                    g_w[first_idx] = f'<b>{g_w[first_idx]}'
                    p_w[first_idx] = f'<b>{p_w[first_idx]}'
                g_w[last_idx] = f'{g_w[last_idx]}</b>'
                p_w[last_idx] = f'{p_w[last_idx]}</b>'

    return g_w, p_w

# e - 5. 띄어쓰기 신경써서 문장 만들어주기
def _work_connect_word(words):
    completed = str()
    for idx, word in enumerate(words):
        # 첫 단어 Capitalize
        if idx == 0:
            if word[0] != '<':
                word = word.capitalize()
                completed += str(word)
            elif word[0] == '<':
                completed += str(word)
        # 마지막 인덱스는 마지막 띄어쓰기 없음 
        elif idx == len(words):
            completed += str(word)
        # 그 외에는 띄어쓰기
        else:
            completed += ' ' + str(word)
            
    return completed

# find diff word
def _diff_word_dark(g_w, p_w):
    # search index 
    search_length = _find_search_length(g_w, p_w)
    first_idx, last_idx = _find_first_idx(g_w, p_w, search_length), _find_last_idx(g_w, p_w, search_length)
    g_w, p_w = _add_b_tag(g_w, p_w, first_idx, last_idx)
    g_sent, p_sent = _work_connect_word(g_w), _work_connect_word(p_w)

    return g_sent, p_sent