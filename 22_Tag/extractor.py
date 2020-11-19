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
def find_directly_close(tag_lists, sent):
    tag_found_end = list()
    tag_found_end_idx = list()
    for sdx in range(0, len(sent)):
        tag_end = ''
        html_tag_start_idx = 0
        html_tag_end_idx = 0
        html_tag_end_is = ''
        html_tag_end_idx_str = ''
        # 태그가 어떻게 생겼는지만 보기
        for html_tag in tag_lists:
            tag_end_two = f'</{html_tag[0]}'
            if sent[sdx:sdx+len(tag_end_two)] != tag_end_two:
                continue
            elif sent[sdx:sdx+len(tag_end_two)] == tag_end_two:
                tag_end = f'</{html_tag}'
                len_html_tag = len(tag_end)
                # 태그의 길이 만큼 찾아보기
                for idx in range(sdx, len(sent)-len_html_tag + 1):
                    # <span 같이 시작 찾기
                    if sent[idx:idx+len_html_tag] == tag_end:
                        # print(f'html_tag_start_idx: {idx}')
                        # print(sent[idx:idx+len_html_tag])
                        html_tag_start_idx = idx
                        for jdx in range(html_tag_start_idx, len(sent)):
                            # > 같이 끝 찾기
                            if sent[jdx] == '>':
                                # print(f'html_tag_end_idx: {jdx}')
                                # print(sent[html_tag_start_idx:html_tag_end_idx])
                                html_tag_end_idx = jdx + 1
                                html_tag_end_is = sent[html_tag_start_idx:html_tag_end_idx]
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