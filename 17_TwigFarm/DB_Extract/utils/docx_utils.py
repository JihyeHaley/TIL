import re
import mammoth


# 숫자와 문자로만 이루어진 의미없는 구문 찾기
def _only_char(text):
    #skip = re.compile('^[0-9『』@%#^&~!★●㎝▪:;()/=+*$,._\\-]+')
    skip = re.compile('^[0-9『』@%#^&~!★● ㎝▪:;()/=+*$,._\\- ]+')
    return bool(skip.fullmatch(text))


# 페이지 넘버 찾기
def _is_page_num(text):
    is_page = re.compile('[0-9|pP[\]{}()<>\s]+')
    return bool(is_page.fullmatch(text))



# mammoth 사용하여 docx raw test parsing
def _read_docx_to_text(file_path, stop_words):
    with open(file_path, "rb") as docx_file:
        result = mammoth.extract_raw_text(docx_file)
        text = result.value  # The raw text
        # messages = result.messages  # Any messages

    contents = text.split("\n")

    contents_prep = []
    for line in contents:
        each_line = line.strip()
        if each_line and not _only_char(each_line) and each_line not in stop_words and \
                not _is_page_num(each_line):
            contents_prep.append(each_line)
    return contents_prep