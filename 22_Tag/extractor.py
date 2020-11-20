from common_function import html_tag_creator

# 시작 한 개 씩
def find_directly_open(html_tag_kinds, sent):
    tag_found_start = list()
    tag_found_start_idx = list()
    tag_lists = list()
    for sdx in range(0, len(sent)):
        tag_start = ''
        html_tag_start_idx = 0
        html_tag_end_idx = 0
        html_tag_start_is = ''
        html_tag_start_idx_str = ''
        # 태그가 어떻게 생겼는지만 보기
        for html_tag in html_tag_kinds:
            tag_start_two = f'<{html_tag[0]}'
            if sent[sdx:sdx+len(tag_start_two)] != tag_start_two:
                continue
            elif sent[sdx:sdx+len(tag_start_two)] == tag_start_two:
                tag_start = f'<{html_tag}'
                len_html_tag = len(tag_start)
                tag_lists.append(html_tag)
                # 태그의 길이 만큼 찾아보기
                for idx in range(sdx, len(sent)-len_html_tag):
                    # <span 같이 시작 찾기
                    if sent[idx:idx+len_html_tag] == tag_start:
                        html_tag_start_idx = idx
                        for jdx in range(html_tag_start_idx, len(sent)-len_html_tag):
                            # > 같이 끝 찾기
                            if sent[jdx] == '>':
                                html_tag_end_idx = jdx + 1
                                html_tag_start_is = sent[html_tag_start_idx:html_tag_end_idx]
                                html_tag_start_idx_str = f'{html_tag_start_idx}:{html_tag_end_idx}'
                                tag_found_start.append(html_tag_start_is)
                                tag_found_start_idx.append(html_tag_start_idx_str)
                                # print(html_tag_start_is)
                                break
                    break       
                break
    return tag_found_start, tag_found_start_idx, tag_lists



# 클로즈 한 개 씩        
def find_directly_close(sent, tag_lists):
    tag_found_end = list()
    tag_found_end_idx = list()
    find_from_here = len(sent)
    for idx, html_tag in enumerate(tag_lists):
        tag_end = f'</{html_tag}'
        len_html_tag = len(tag_end)
        for sdx in range(find_from_here, 0, -1):
            html_tag_start_idx = 0
            html_tag_end_idx = 0
            html_tag_end_is = ''
            html_tag_end_idx_str = ''
            if sent[sdx-len_html_tag-1:sdx-1] != tag_end:
                continue
            elif sent[sdx-len_html_tag-1:sdx-1] == tag_end:
                find_from_here = sdx-1
                print(sent[sdx-len_html_tag-1:sdx-1])
                for idx in range(sdx, 0, -1):
                    html_tag_start_idx = sdx - len_html_tag - 1
                    for jdx in range(html_tag_start_idx, len(sent)):
                        # > 같이 끝 찾기
                        if sent[jdx] == '>':
                            print(f'html_tag_end_idx: {jdx}')
                            html_tag_end_idx = jdx + 1
                            html_tag_end_is = sent[html_tag_start_idx:html_tag_end_idx]
                            print(f'html_tag_end_is: {html_tag_end_is}')
                            html_tag_end_idx_str = f'{html_tag_start_idx}:{html_tag_end_idx}'
                            tag_found_end.append(html_tag_end_is)
                            tag_found_end_idx.append(html_tag_end_idx_str)
                            break
                    break       
                break
     
    return tag_found_end, tag_found_end_idx




# 1개의 문장을 넣어주기 (str로 input)
def find_tag(sent):
    
    # 태그 리스트 가져오기 (어떤 태그가 있는지 모르니깐 다 찾아주기)
    html_tag_kinds = html_tag_creator()
    # 태그 종류별로 탐색 (일단 1개만 찾아보기)
    
    html_tag_start, html_tag_start_idx, tag_lists = find_directly_open(html_tag_kinds, sent)
    html_tag_end, html_tag_end_idx = find_directly_close(tag_lists, sent)

    return html_tag_start, html_tag_start_idx, html_tag_end, html_tag_end_idx

# check the list 
def chceck_find_list(tag_found_start, tag_found_start_idx, tag_found_close, tag_found_close_idx):
    if len(tag_found_start) >= 1:
        tag_found_close_pre = list()
        tag_found_close_idx_pre = list()
        a = tag_found_start[0] 
        b = tag_found_close[0]

        # 태그의 시작
        if a[1:2] != b[2:3]:
            for _ in range(len(tag_found_start)):
                standard = tag_found_start[_]
                # </ 뺀 's', 'a', 'h'
                comparison = tag_found_close[_][2:3]
                if tag_found_close[_][2:3] in standard:
                    continue

                elif comparison not in standard:
                    for __ in range(len(tag_found_start), 0, -1): 
                        subject_1 = tag_found_close.pop()
                        subject_2 = tag_found_close_idx.pop()
                        if comparison in standard:
                            tag_found_close_pre.append(subject_1)
                            tag_found_close_idx_pre.append(subject_2)
                        elif comparison not in standard:
                            tag_found_close.append(subject_1)
                            tag_found_close_idx.append(subject_2)
                    
            tag_found_close = tag_found_close_pre 
            tag_found_close_idx = tag_found_close_idx_pre 
            return tag_found_start, tag_found_start_idx, tag_found_close, tag_found_close_idx

        elif a[1:2] == b[2:3] :
            return tag_found_start, tag_found_start_idx, tag_found_close, tag_found_close_idx
