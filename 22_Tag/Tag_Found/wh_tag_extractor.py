import re

tags = re.compile(r'(<\w+_?\d*>)|</\w+>')


# 문장 내에 있는 태그 모양새를 모두 추출
def _find_all(sentence, ls=[], start_idx=0):
    global tags
    tag = re.search(tags, sentence)    # 문자열에서의 tag의 범위를 찾기 위해 re.search 사용
    if not tag: # tag가 없는 문장이면 함수 멈춤. 재귀 함수의 멈춤 조건이기도 하다.
        return
    tag_range = tag.span()
    start_idx += tag_range[0]
    end_idx = start_idx + (tag_range[1]-tag_range[0])
    ls.append((tag.group(), (start_idx, end_idx)))
    return _find_all(sentence[tag_range[1]:], ls, end_idx)    # search는 find_all이 안 되므로 재귀적으로 모두 찾는다.


# waiting_list에서 닫힘 태그의 짝을 찾아주는 함수
def _find_pair(waiting_list, i, close_tag_name):
    if not waiting_list:
        return False
    open_tag_name = waiting_list[i][0].split(' ')[0].split('_')[0].split('>')[0][1:]
    if open_tag_name == close_tag_name:
        return True
    return False


# main 함수
def find_all_tag_pairs(sentence):
    sentence_tags = []     # 문장 내에 있는 태그 꼴을 담을 리스트
    waiting_list = []      # open_tag를 넣을 stack
    paired_tags = []       # 올바르게 짝지어진 태그들을 담을 리스트
    _find_all(sentence, sentence_tags)    # 함수가 돌면서 sentence_tags안에 tag꼴이 모두 담긴다. 
    if not sentence_tags:  # 문장 내에 태그가 하나도 없으면 빈 리스트 반환
        return []
    for tag in sentence_tags:    # 'tag' == (tag_full, (tag_start_index, tag_end_index)) 꼴의 tuple object
        tag_close = False
        # tag의 open/close 여부를 판단해서 open_tag면 stack에 넣는다.
        if tag[0].startswith('</'): tag_close = True
        else: waiting_list.append(tag)
            
        if tag_close:
            close_tag_name = tag[0][2:-1]
            paired = False
            if len(waiting_list) <= 1: r = range(0, 1)  # len(waiting_list)==1일 경우 아래와 같이 계산하면 range가 돌지 않는다
            else: r = range(len(waiting_list)-1,-1,-1)  # waiting_list의 마지막 요소부터 가져온다.
            for i in r:
                paired = _find_pair(waiting_list, i, close_tag_name)
                if paired: 
                    flag = i
                    break
            if paired:
                paired_tags.append((waiting_list[flag], tag))
                waiting_list.pop(flag)    # 올바르게 짝지어진 열림 태그는 waiting_list에서 제거해준다.
            else:
                print(f'There is an unpaired closing tag: {tag}')   # 열림 태그가 없는 닫힘 태그일 경우 에러 메시지 출력
                
    for tag in waiting_list:    # waiting_list에는 짝지어지지 못한 열림 태그가 남아있다. 이는 Self-close로 처리.
        paired_tags.append((tag, ('Self-Close', (tag[1][1]+1, -1))))  # self-close의 범위는 임의로 처리
        
    return sorted(paired_tags, key =(lambda x: x[0][1][0]))    # 태그가 시작하는 index에 맞추어서 정렬
    
        