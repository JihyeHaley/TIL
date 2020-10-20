###############################################################
######sentence
# sentence 처음쓰기 새로쓰기
def raw_sents_input_new():
    n = int(input('문장을 몇번 입력 받으실래요? '))
    print('단어를 더이상 입력하기 싫으면 0을 눌러주세요')
    new_sents_log = open(f'./18_Natural_Processing/공학_raw_input.txt', 'w')
    for i in range(n):
        if i == 0:
            print(f'sample로 {n}개만 먼저 input받습니다.')
        print(f'{str(i+1)}/{n}개')
        a = str(input('Input your sent: '))
        if a == '0':
            break
        sentence = a + '\n'
        new_sents_log.write(sentence)
    new_sents_log.close()  


def raw_sents_input_append():
    n = int(input('문장을 몇번 입력 받으실래요? '))
    print('단어를 더이상 입력하기 싫으면 0을 눌러주세요')
    append_sent_log = open(f'./NIA_DICT/공학_raw_sentence_input_collecting.txt', 'a')
    
    for i in range(n):
        print(f'{str(i+1)}/{n}개')
        a = str(input('Input your sent: '))
        if a == '0':
            break
        sentence = a + '\n'
        append_sent_log.write(sentence)
    append_sent_log.close() 


