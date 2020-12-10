from nltk.tokenize import sent_tokenize
import stanza
import re

# Downloads language models
stanza.download('en')
stanza.download('ko')
stanza.download('ja')
stanza.download('zh')

# STANZA Support Languages
SUPPORT_LANGUAGE = ['zh', 'ja', 'ko', 'en']

GCON_TAG = 'gcon_'

RE_INT = re.compile(r'^([1-9]\d*|0)[.]{0,1}$')
RE_FORBIDDEN_CHARACTER = re.compile(r'^[gcon_.,!@#$%^&*()`\'\"]{1}$')

tokenizer_ko = stanza.Pipeline(lang='ko', processors='tokenize')
tokenizer_en = stanza.Pipeline(lang='en', processors='tokenize')
tokenizer_ja = stanza.Pipeline(lang='ja', processors='tokenize')
tokenizer_zh = stanza.Pipeline(lang='zh', processors='tokenize')

STANZA_TOKENIZER_DICT = {
    'ko': tokenizer_ko,
    'en': tokenizer_en,
    'ja': tokenizer_ja,
    'zh': tokenizer_zh
}


def tokenize_nltk(sentence):
    return sent_tokenize(sentence)


def tokenize_stanza(sentence, source_language_code):
    doc = STANZA_TOKENIZER_DICT.get(str(source_language_code))(sentence)
    # tokenizer = stanza.Pipeline(lang=source_language_code, processors='tokenize')
    # doc = tokenizer(sentence)
    return [sentence.text for sentence in doc.sentences]


# '\n' 기준으로 텍스트를 문장 list 로 변경
def convert_texts(text):
    return [x.strip().strip(u'\u200b') for x in text.split('\n')]


# 문장 list 내의 요소 문장을 sentence tokenizer로 필요시 여러 문장으로 나누고, index, text 로 이루어진 sentences list 로 변경
def tokenize_sentences(texts, source_language_code):
    tokenized_texts = []
    sentences = []
    for text in texts:
        if source_language_code in SUPPORT_LANGUAGE:
            tokenized_sentence = tokenize_stanza(text, source_language_code)
        else:
            tokenized_sentence = tokenize_nltk(text)
        tokenized_texts.extend(tokenized_sentence)

    # 결과값의 시작 index의 값은 0
    for index, value in enumerate(tokenized_texts):
        if re.match(RE_INT, value) is None and re.match(RE_FORBIDDEN_CHARACTER, value) is None:
            sentences.append({'index': index, 'text': value.strip()})

    return sentences


# 원문 문서 내의 원문 문장이 tag 로 대체되는 문서로 변경
def convert_formatted_document(document, sentences):
    formatted_text = document
    for sentence in sentences:
        index = sentence['index']
        text = sentence['text']
        if formatted_text.find(text) < 0:
            text = text.replace("\"", "\\\"")
        if formatted_text.find(text) < 0:
            print('convert_formatted_document - not found!!!')
            print(text)
        formatted_text = formatted_text.replace(text, f"<{GCON_TAG}{index}>", 1)
    return formatted_text


# tag 포함된 문서와 번역 결과 list를 기반으로 번역 문서로 변경
def convert_translated_document(formatted_document, translated):
    translated_document = formatted_document
    for sentence in translated:
        index = sentence["index"]
        tag = f"<{GCON_TAG}{index}>"
        target = sentence["tgt"]
        translated_document = translated_document.replace(tag, target, 1)
    return translated_document

# {'text': text.strip(), 'index': self.idx}


if __name__ == "__main__":
    test_text = """
        a. 안녕하세요.
        1. 좋은 아침입니다.
        ㄱ. 초 록
        가. 바이.
        II. 그게 뭐예요?
        ぁ. 잘 부탁드립니다.
        ㊿. 과연 될 것인가?
        ⓐ. 수고하셨습니다.
        ⓰. 까만 동그라미도 되나요?
        ㉻. 이젠 에어컨이 잘 나오네요.
        (가). 괄호는 안되겠죠.
    """

    test_text_ja = """
    1.マイケルユージーンアーチャー[1]（1974年2月11日生まれ）は、彼のステージ名D'Angelo（ディアンジェロと発音）でよく知られ、アメリカのシンガー、ソングライター、マルチ楽器奏者、レコードプロデューサーです。 
    ダンジェロは、エリカバドゥ、ローリンヒル、マックスウェル、コラボレーターのアンジーストーンなどのアーティストとともに、ネオソウルムーブメントに関連しています。
    2.ペンテコステ派の息子、バージニア州リッチモンドに生まれる
    ダンジェロ牧師は子供の頃ピアノを学びました。18歳の彼は、ハーレムのアポロ劇場で3週間連続してアマチュアの才能コンテストに優勝しました。ヒップホップグループI.D.U.との短い提携の後、彼の最初の大きな成功は、1994年に「U Will Know」という歌の共同作家および共同プロデューサーとして生まれました。
    """
    #
    text_zh = """
         电影《甜蜜蜜》由陈可辛导演，张曼玉、黎明和曾志伟主演，1996年公映? 1996年正值香港回归前夕，也是一代歌后邓丽君逝世翌年。电影借助这一特殊时代背景，讲述了20世纪末期香港新移民的艰辛岁月，并以邓丽君的歌曲《甜蜜蜜》贯穿始终，成功抓住两岸三地中国人的共通情感。影片剧情始于1986年，终于1995年邓丽君骤逝当天，在中国出现移民潮的大背景下，通过小人物的命运展现了香港回归前十年的历史变迁。
        """

    test_text_ko = '1. 제목\n 내 이름은 백선호입니다. 백선호입니다. 고맙습니다. 저는 NLP 논문을 읽고 공부를 하는 것을 좋아 합니다.'
    test_text_ko1 = 'A씨는 국내 판매책을 고용한 뒤, 인터넷을 통해 구매자들에게 연락이 오면 필로폰을 0.1g, 0.5g, 1g 등의 단위로 포장해 일정한 장소에 숨겨 놓은 후 사진으로 촬영해 필로폰 구매자가 찾아갈 수 있도록 전송하는 속칭 \'던지기 방식\'으로 필로폰을 판매한 것으로 조사됐다.'
    test_text_ko2 = '메디톡스가 보툴리눔 톡신 제제 \'메디톡신\'의 품목허가 취소로 창사 이래 최대 위기를 맞았다. 메디톡신은 메디톡스의 연간 매출 40%를 차지하는 주력 제품이다.'

    # test_text = """
    #     Hello again, Miss Dunbar. I’m afraid you’re not having a very pleasant holiday. He motioned for her to sit.
    #     People do seem to be dying in my vicinity,” she said.
    # """
    # text = '①. 슬로건 및 비전 : 가까이 두고 싶은 정보 친구가 되자 ex_아이언맨에 등장하는 비전,'

    document = test_text
    print('##### DOCUMENT #####')
    print(document)

    texts = convert_texts(document)
    # print('##### TEXTS #####')
    # print(texts)

    sentences = tokenize_sentences(texts, 'ko')
    print('##### SENTENCES #####')
    print(sentences)

    # formatted_document = convert_formatted_document(document, sentences)
    # print('##### FORMATTED_DOCUMENT #####')
    # print(formatted_document)
