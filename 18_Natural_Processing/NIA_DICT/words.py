###############################################################
###### word

# word 처음쓰기 새로쓰기
def raw_words_input_new():
    n = int(input('단어를 몇번 입력 받으실래요? '))
    print('단어를 더이상 입력하기 싫으면 0을 눌러주세요')
    new_words_log = open('/Users/jihyeoh/desktop/GIT/TIL/18_Natural_Processing/02_raw_word_input_collecting.txt', 'w')
    for i in range(n):
        if i == 0:
            print(f'sample로 {n}개만 먼저 input받습니다.')
        print(f'{str(i+1)}/{n}개')
        a = str(input('Input your word: '))
        if a == '0':
            break
        word = a + '\n'
        new_words_log.write(word)
    new_words_log.close()  


# word 이어쓰기
def raw_words_input_append():
    n = int(input('단어를 몇번 입력 받으실래요? '))
    print('단어를 더이상 입력하기 싫으면 0을 눌러주세요')
    append_words_log = open(f'./02_raw_word_input_collecting.txt', 'a')
    for i in range(n):
        print(f'{str(i+1)}/{n}개')
        a = str(input('Input your word: '))
        if a == '0':
            break
        word = a + '\n'
        append_words_log.write(word)
    append_words_log.close()  


# word 전처리 갖고놀기
def raw_words_preprocessing():
    with open('./02_raw_word_input_collecting.txt', 'r') as raw_sents:
        raw_sents = raw_sents.readlines()
        # raw_sentences = [print(idx, _.strip('\n')) for idx, _ in enumerate(raw_sentences)]
        raw_sents = [_.strip('\n') for _ in raw_sents]
    return raw_sents
