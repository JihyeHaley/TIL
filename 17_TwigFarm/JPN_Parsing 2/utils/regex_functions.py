'''
    정규식 관련 함수 모음
'''

import re

# 한글 / 영어 둘다 아닌 경우
def neitherKoNorEn(text):
    neither = re.compile('((?![ㄱ-ㅣ가-힣|a-zA-Z]).)*')
    return bool(neither.fullmatch(text))


# 한글이 포함되지 않은 경우
def mustEnglish(text):
    never_ko = re.compile('((?![ㄱ-ㅣ가-힣]).)*')
    return bool(never_ko.fullmatch(text))


# 영어가 포함되어있는 경우
def isEnglish(text):
    en = re.compile('.*[a-zA-Z]+')
    # return bool(ko.fullmatch(text))
    return bool(en.match(text))


# 한글이 포함되어있는 경우
def isKorean(text):
    ko = re.compile('.*[ㄱ-ㅣ가-힣]+')
    # return bool(ko.fullmatch(text))
    return bool(ko.match(text))


#3개의 알파벳 이상 기준으로 split
def split_kor_eng(text):
    # return re.split(r'(.?[a-zA-Z]{2}.*)', text)
    return re.split(r'([a-zA-Z]{3}.*)', text)


# SI.H added
def split_kor_eng_v2(text):
    ko_text = ""
    en_text = ""
    for part_text in re.split(r"([a-zA-Z]{1,}.*)", text):
        # only eng
        if part_text.strip() and not isKorean(part_text):
            en_text += part_text
        #  kor or kor/Eng
        elif part_text.strip() and isKorean(part_text):
            ko_text += part_text

    return [ko_text, en_text]


# 숫자와 문자로만 이루어진 의미없는 구문 찾기
def only_char(text):
    #skip = re.compile('^[0-9『』@%#^&~!★●㎝▪:;()/=+*$,._\\-]+')
    skip = re.compile('^[0-9『』@%#^&~!★● ㎝▪:;()/=+*$,._\\- ]+')
    return bool(skip.fullmatch(text))


# 10p 와 같은 페이지 넘버 찾기
def is_page_num(text):
    is_page = re.compile('[0-9|pP[\]{}()<>\s]+')
    return bool(is_page.fullmatch(text))


# pattern의 regex를 text에서 찾아 지움
def remove_regex(pattern, text):
    if re.search(pattern, text):
        return re.sub(pattern, '', text)
    return text


# text가 pattern을 full match 되는지 체크
def check_fullmatch(pattern, text):
    return bool(pattern.fullmatch(text))

# quotation mark regex - modified unify_quotes (by WH.G)
def quotes_cleaner(text):
    text = re.sub(r'[“”„‟❝❞⹂〝〞〟]', '"', text)
    text = re.sub(r"[‘’‛❛❜]", "'", text)
    return text


# 문장사이 띄어쓰기, 공백제거, 웹사이트/전화번호/날짜/시간 제거
def regex_cleaner(text):    
    
    # 대놓고 특수문자 지워버리기
    special_char_regex = re.compile(r'[■□ㅇ❍○©▶▸①②③④⑤※]')
    text = remove_regex(special_char_regex, text)

    # 일반 웹사이트 주소 지우기
    web_regex = re.compile(r'((http)s{0,1}://)?[\s]{0,1}[-a-z0-9]{0,3}\.{0,1}[-a-z0-9@:%._\\+~#=]{2,256}\.[a-z]{2,4}(/[a-z\-_\.?0-9=]*)*',
                           re.IGNORECASE)
    text = remove_regex(web_regex, text)
    
    
    # 이메일주소 지우기
    email_regex = re.compile(r'([a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}.{0,1}\w{0,4})', re.IGNORECASE)
    text = remove_regex(email_regex, text)
    
    
    # 전화번호 지우기 - 021231234(5), (02(2)-123(3)-1234), (02)988-9873, 1234-1234 
    phone_regex = re.compile(r'[\[<{\(]{0,1}(([\[<{\(]{0,1}[\☎\☏]{0,1}[\s]{0,1}[0-9]{0,3}[}>\)\]]{0,1}\-{0,1}[0-9]{3,4}\-{0,1}[0-9]{3,4})|([0-9]{9,10}))[}>\)\]]{0,1}')
    text = remove_regex(phone_regex, text)
    
    
    # 시간 지우기 - (10:00, 11:00, 14:00, 15:00, 16:00) / 1:00 ~ 12:00
    time_regex = re.compile(r'[\[<{\(]{0,1}([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9][,\-~\s]{0,2}[}>\)\]]{0,1}')
    text = remove_regex(time_regex, text)
    
    
    # 날짜 지우기 - yyyy.mm.dd | mm.dd.yyyy | dd.mm.yyyy
    date_regex = r'((\d{4})([\s./-]{0,3})(0[1-9]|1[012]|[1-9])([\s./-]{0,3})(0[1-9]|[12][0-9]|3[0-1]|[1-9])([\s./-]{0,3}))'\
                '|((0[1-9]|1[012]|[1-9])([\s./-]{0,3})(0[1-9]|[12][0-9]|3[0-1]|[1-9])([\s./-]{0,3})(\d{4})([\s./-]{0,3}))'\
                '|((0[1-9]|[12][0-9]|3[0-1]|[1-9])([\s./-]{0,3})(0[1-9]|1[012]|[1-9])([\s./-]{0,3})(\d{4})([\s./-]{0,3}))'
    text = remove_regex(date_regex, text)

    
    # 소제목 분류 - Ⅳ.  실증분석 or 1. 표본의 특성
    title_regex = re.compile(r'((^\d\.|[Ⅰ|II|Ⅱ|Ⅲ|Ⅳ|Ⅴ]\.)(\d\.){0,})\s{0,}([\D[ㄱ-ㅣ가-힣|a-zA-Z].*)')
    text = re.sub(title_regex, r"\1\4", text)


    # 문장과 문장사이에 . 있을때 띄어쓰기가 없다면 띄어쓰기 해줌
    text = re.sub(r'([ㄱ-ㅣ가-힣|a-zA-Z|0-9])\.([ㄱ-ㅣ가-힣|a-zA-Z|0-9])', r'\1. \2', text)
    
    
    #정제된 문장에 한/영이 없으면 지우자
    if neitherKoNorEn(text):
        return ""
    
    return text


#  JH.O - 정규식 작업 1
def pptx_extra_regex(raw):
    # 대놓고 특수문자 지워버리기
    raw = re.sub(r'(\s?■\s?)|(‘|※|「|」|`|･|ㅇ|□|❍|▶|▸|»|•|©|—|○|\(\)|-|\*|α|β)\s*', '', raw)
    # index 특수문자 지원버리기
    raw = re.sub(r'①|②|③|④|⑤', '', raw)
    # 알파벳 하나만 덩그러니 있으면 삭제
    raw = re.sub(r"\d{1,2}\.\s?", "", raw)
    # … 제거
    raw = re.sub(r'…+', '', raw)
    # # . 숫자 지우기
    # raw = re.sub(r'\.\s{1}\d{1,2}', '', raw)
    # . 으로 된 목차 다 지우기
    # raw = re.sub(r'\.{2,}\s?\d{1,2}', '', raw)
    # . 다 지우기
    raw = re.sub(r'\.{2,}', '', raw)
    # 주석으로 처리되는 아이들 지우기
    raw = re.sub(r"(ISOfocus|ISO(f포커스|포커스))_?\d{1,3}\s*\|\s*\d{1,2}", "", raw)
    raw = re.sub(r"\s{1}\|\s{1}(ISOfocus|ISO포커스){1}_{1}\d{1,3}", "", raw)
    raw = re.sub(r" – ISO \| ", "", raw)
    # 몇 장 삭제
    raw = re.sub(r"제\d{1,2}장", "", raw)
    # 챕터 삭제
    raw = re.sub(r"(C|c)h(\.\s)?apter\s?\d{1,3}", "", raw)
    # space bar 너무 많으면 버리기
    raw = re.sub(r"\s{2,}", "", raw)
    # '.'뒤에 스페이스 주기 (혹시 2개 있을수도 있어서 *로 처리)
    raw = re.sub(r"\.\s{1,2}", ". ", raw)
    # 날짜 제거
    raw = re.sub(r"(\d{2,4}(년|\.|/)\s*)\d{1,2}(월|\.|/)\s*\d{1,2}(일|\s*)", ". ", raw)
    # 상표 지우기
    raw = re.sub(r"(㉿|®|©){1}\w+", ". ", raw)
    # 숫자만 제일 앞에 있으면 버리기
    raw = re.sub(r"^\d{1,3}\.?", "", raw)

    # 전화번호(T+, M+ Mobile)
    raw = re.sub(r'(	\+)?(T|M|Fax|FAX){1}(T \+|Fax	\+|Fax	\+|T	\+)?/d{1,}/s?/d{1,/s?(/d{1,3})?', '', raw)
    # 눈에 띄었던 예외()
    raw = re.sub(r'(level){1}\s{1}\d{1}', '', raw)
    # 숫자가 무더기로있는 경우
    raw = re.sub(r'^\(?\d{1,3}(\s?\d{3})?\)?', '', raw)

    # 영문 들어간 날짜 지우기
    date_regex_2 = r"((January|Feburary|March|April|May|June|July|August|September|October|November|December)|(Jan|Feb|Mar|Apr|Aug|Sep|Oct|Nov|Dec))/s?(\.|,)?\s?/d{1,2}/s?(\.|,)?/d{1,2}"
    raw = re.sub(date_regex_2, "", raw)

    return raw

#  JH.O - 정규식 작업 2
def pdf_extra_regex(raw):
    # 대놓고 특수문자 지워버리기
    raw = re.sub(r'(\s?■\s?)|(‘|※|「|」|`|･|ㅇ|□|❍|▶|▸|»|•|©|—|○|\(\)|-|\*|α|β)\s*', '', raw)
    # index 특수문자 지원버리기
    raw = re.sub(r'①|②|③|④|⑤', '', raw)
    # 알파벳 하나만 덩그러니 있으면 삭제
    raw = re.sub(r"\d{1,2}\.\s?", "", raw)
    # … 제거
    raw = re.sub(r'…+', '', raw)
    # # . 숫자 지우기
    # raw = re.sub(r'\.\s{1}\d{1,2}', '', raw)
    # . 으로 된 목차 다 지우기
    # raw = re.sub(r'\.{2,}\s?\d{1,2}', '', raw)
    # . 다 지우기
    raw = re.sub(r'\.{2,}', '', raw)
    # 주석으로 처리되는 아이들 지우기
    raw = re.sub(r"(ISOfocus|ISO(f포커스|포커스))_?\d{1,3}\s*\|\s*\d{1,2}", "", raw)
    raw = re.sub(r"\s{1}\|\s{1}(ISOfocus|ISO포커스){1}_{1}\d{1,3}", "", raw)
    raw = re.sub(r" – ISO \| ", "", raw)
    # 몇 장 삭제
    raw = re.sub(r"제\d{1,2}장", "", raw)
    # 챕터 삭제
    raw = re.sub(r"(C|c)h(\.\s)?apter\s?\d{1,3}", "", raw)
    # space bar 너무 많으면 버리기
    raw = re.sub(r"\s{2,}", "", raw)
    # '.'뒤에 스페이스 주기 (혹시 2개 있을수도 있어서 *로 처리)
    raw = re.sub(r"\.\s{1,2}", ". ", raw)
    # 날짜 제거
    raw = re.sub(r"(\d{2,4}(년|\.|/)\s*)\d{1,2}(월|\.|/)\s*\d{1,2}(일|\s*)", ". ", raw)
    # 상표 지우기
    raw = re.sub(r"(㉿|®|©){1}\w+", ". ", raw)
    # 숫자만 제일 앞에 있으면 버리기
    raw = re.sub(r"^\d{1,3}\.?", "", raw)

    # 전화번호(T+, M+ Mobile)
    raw = re.sub(r'(	\+)?(T|M|Fax|FAX){1}(T \+|Fax	\+|Fax	\+|T	\+)?/d{1,}/s?/d{1,/s?(/d{1,3})?', '', raw)
    # 눈에 띄었던 예외()
    raw = re.sub(r'(level){1}\s{1}\d{1}', '', raw)
    # 숫자가 무더기로있는 경우
    raw = re.sub(r'^\(?\d{1,3}(\s?\d{3})?\)?', '', raw)

    # 영문 들어간 날짜 지우기
    date_regex_2 = r"((January|Feburary|March|April|May|June|July|August|September|October|November|December)|(Jan|Feb|Mar|Apr|Aug|Sep|Oct|Nov|Dec))/s?(\.|,)?\s?/d{1,2}/s?(\.|,)?/d{1,2}"
    raw = re.sub(date_regex_2, "", raw)

    return raw
