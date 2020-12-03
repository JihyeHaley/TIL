'''
    정규식 관련 함수 모음
'''

import re

# 한글 / 영어 둘다 아닌 경우
def neitherKoNorEn(text):
    neither = re.compile(r'((?![가-힣a-zA-Z]).)*')
    return bool(neither.fullmatch(text))


# 한글이 포함되지 않은 경우
def mustEnglish(text):
    never_ko = re.compile(r'((?![ㄱ-ㅣ가-힣]).)*')
    return bool(never_ko.fullmatch(text))


# 영어가 포함되어있는 경우
def isEnglish(text):
    en = re.compile(r'.*[a-zA-Z]+') #([a-zA-Z]+)+
    # return bool(ko.fullmatch(text))
    return bool(en.match(text))


# 한글이 포함되어있는 경우
def isKorean(text):
    ko = re.compile(r'.*[ㄱ-ㅣ가-힣]+')
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
    skip = re.compile(r'^[0-9『』@%#^&~!★●㎝▪:;()/=+*$,._\\\- ■□❍○©▶▸①②③④⑤※「」･ㅇ□❍▶▸»•©—○αβ↳]+$')
    return bool(skip.fullmatch(text))


# 10p 와 같은 페이지 넘버 찾기
def is_page_num(text):
    is_page = re.compile(r'[0-9|pP[\]{}()<>\s]+')
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


# specific regex handler for docx_single and pdf
def regex_cleaner_ko(text):
    # 문장 시작 특수문자 삭제
    special_start_regex = re.compile(r'^[\s–·『』@%#^&~!★●㎝▪:;/=+*$,._\\\-■□○©▶▸①②③④⑤※「」･ㅇ□❍»•©—○αβ↳→]+')
    text = re.sub(special_start_regex, '', text).strip()

    # 일반 웹사이트 주소 지우기
    web_regex = re.compile(r'((http)s{0,1}://)?[\s]{0,1}[-a-z0-9]{0,3}\.{0,1}[-a-z0-9@:%._\\+~#=]{2,256}\.[a-z]{2,4}', re.IGNORECASE)
    text = re.sub(web_regex, '', text).strip()

    # 이메일주소 지우기
    email_regex = re.compile(r'([a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}.{0,1}\w{0,4})', re.IGNORECASE)
    text = re.sub(email_regex, '', text).strip()

    # 전화번호 지우기 - 021231234(5), (02(2)-123(3)-1234), (02)988-9873, 1234-1234
    phone_regex = re.compile(
        r'[\[<{\(]{0,1}(([\[<{\(]{0,1}[\☎\☏]{0,1}[\s]{0,1}[0-9]{0,3}[}>\)\]]{0,1}\-{0,1}[0-9]{3,4}\-{0,1}[0-9]{3,4})|([0-9]{9,10}))[}>\)\]]{0,1}')
    text = re.sub(phone_regex, '', text).strip()

    # # 소제목 분류 - Ⅳ.  실증분석 or 1. 표본의 특성 -> Ⅳ.실증분석 or 1.표본의 특성
    # title_regex = re.compile(r'((^\d\.|[Ⅰ|II|III|Ⅱ|Ⅲ|Ⅳ|Ⅴ|IV|V|VI]\.)(\d\.){0,}|^\d{1,}\))\s{0,}([\D[ㄱ-ㅣ가-힣|a-zA-Z].*)')
    # text = re.sub(title_regex, r"\1\4", text)

    # 정제된 문장에 한/영이 없으면 삭제
    if neitherKoNorEn(text):
        return ""

    return text


# 문장사이 띄어쓰기, 공백제거, 웹사이트/전화번호/날짜/시간 제거
def regex_cleaner(text):

    # 문장시작이 특수문자 삭제
    special_start_regex = re.compile(r'^([→–■‘※「」`･·ㅇ□❍▶▸»•©—○@%#^&~!\)\*\s『』★●㎝▪□○①②③④⑤※「」･↳])*')
    text = re.sub(special_start_regex, '', text).strip()

    # 소제목 분류 - Ⅳ.  실증분석 or 1. 표본의 특성 띄어쓰기 붙이기 -> Ⅳ.실증분석 or 1.표본의 특성
    title_regex = re.compile(r'((^\d\.|[Ⅰ|II|III|Ⅱ|Ⅲ|Ⅳ|Ⅴ|IV|V|VI]\.)(\d\.){0,}|^\d{1,}\))\s{0,}([\D[ㄱ-ㅣ가-힣|a-zA-Z].*)')
    text = re.sub(title_regex, r"\1\4", text)

    # 이메일주소 지우기
    email_regex = re.compile(r'([a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}.{0,1}\w{0,4})', re.IGNORECASE)
    text = re.sub(email_regex, '', text).strip()

    # multi space remove
    text = re.sub(r'(\s{2,})', ' ', text).strip()

    # 정제된 문장에 한/영이 없으면 삭제
    if neitherKoNorEn(text):
        return ""

    return text


#  JH.O - 정규식 작업
def pptx_extra_regex(raw):

    # # index 특수문자 지원버리기
    # raw = re.sub(r'①|②|③|④|⑤', '', raw)

    # # 알파벳 하나만 덩그러니 있으면 삭제
    # raw = re.sub(r"\d{1,2}\.\s?", "", raw)

    # # … 제거
    # raw = re.sub(r'…+', '', raw)

    # # . 다 지우기
    # raw = re.sub(r'\.{2,}', '', raw)

    # space bar 너무 많으면 버리기
    raw = re.sub(r"\s{2,}", "", raw)

    # 주석으로 처리되는 아이들 지우기
    raw = re.sub(r"(ISOfocus|ISO(f포커스|포커스))_?\d{1,3}\s*\|\s*\d{1,2}", "", raw)
    raw = re.sub(r"\s{1}\|\s{1}(ISOfocus|ISO포커스){1}_{1}\d{1,3}", "", raw)
    raw = re.sub(r" – ISO \| ", "", raw)

    # 몇 장 삭제
    raw = re.sub(r"제\d{1,2}장", "", raw)
    # 챕터 삭제
    raw = re.sub(r"(C|c)h(\.\s)?apter\s?\d{1,3}", "", raw)

    # # 날짜 제거
    # raw = re.sub(r"(\d{2,4}(년|\.|/)\s*)\d{1,2}(월|\.|/)\s*\d{1,2}(일|\s*)", ". ", raw)
    # # 상표 지우기
    # raw = re.sub(r"(㉿|®|©){1}\w+", ". ", raw)
    #
    # # 전화번호(T+, M+ Mobile)
    # raw = re.sub(r'(	\+)?(T|M|Fax|FAX){1}(T \+|Fax	\+|Fax	\+|T	\+)?/d{1,}/s?/d{1,/s?(/d{1,3})?', '', raw)
    # # 눈에 띄었던 예외()
    # raw = re.sub(r'(level){1}\s{1}\d{1}', '', raw)
    # # 숫자가 무더기로있는 경우
    # raw = re.sub(r'^\(?\d{1,3}(\s?\d{3})?\)?', '', raw)
    #
    # # 영문 들어간 날짜 지우기
    # date_regex_2 = r"((January|Feburary|March|April|May|June|July|August|September|October|November|December)|(Jan|Feb|Mar|Apr|Aug|Sep|Oct|Nov|Dec))/s?(\.|,)?\s?/d{1,2}/s?(\.|,)?/d{1,2}"
    # raw = re.sub(date_regex_2, "", raw)

    return raw


# 웹사이트, 전화번호, 날짜, 시간만 있는 경우 지우기, 문장 중간이면 그냥 원래 text return
def del_if_only_WebDateTimeNum(ori_text):

    text = quotes_cleaner(ori_text)

    # 웹사이트 주소 지우기 with parameter
    web_regex = re.compile(r'((http)s{0,1}://)?\s{0,1}((www){0,1}|[a-z0-9]{0,})\.{0,1}[a-z0-9:\-%_\\+~#=]{2,256}\.[a-z]{2,4}(?!\s)(/[a-zA-Z\-_\.?0-9=&]+)*', re.IGNORECASE)
    text = re.sub(web_regex, '', text).strip()

    # 전화번호 지우기 - (02(2)-123(3)-1234), (02)988-9873, 1234-1234, 021231234(5)
    phone_regex = re.compile(r'[\[<{\(]{0,1}(([\[<{\(]{0,1}[\☎\☏]{0,1}[\s]{0,1}[0-9]{0,3}[}>\)\]]{0,1}\-{0,1}[0-9]{3,4}\-{0,1}[0-9]{3,4})|([0-9]{9,10}))[}>\)\]]{0,1}')
    text = re.sub(phone_regex, '', text).strip()

    # 시간 지우기 - (10:00, 11:00, 14:00, 15:00, 16:00) / 1:00 ~ 12:00
    time_regex = re.compile(r'[\[<{\(]{0,1}([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9][,\-~\s]{0,2}[}>\)\]]{0,1}')
    text = re.sub(time_regex, '', text).strip()

    # 날짜 지우기 - yyyy.mm.dd | mm.dd.yyyy | dd.mm.yyyy
    date_regex = r'((\d{4})([\s./-]{0,3})(0[1-9]|1[012]|[1-9])([\s./-]{0,3})(0[1-9]|[12][0-9]|3[0-1]|[1-9])([\s./-]{0,3}))'\
                '|((0[1-9]|1[012]|[1-9])([\s./-]{0,3})(0[1-9]|[12][0-9]|3[0-1]|[1-9])([\s./-]{0,3})(\d{4})([\s./-]{0,3}))'\
                '|((0[1-9]|[12][0-9]|3[0-1]|[1-9])([\s./-]{0,3})(0[1-9]|1[012]|[1-9])([\s./-]{0,3})(\d{4})([\s./-]{0,3}))'
    text = re.sub(date_regex, '', text).strip()

    if only_char(text):
        return ''
    elif len(text) < 5:
        return ''

    return ori_text