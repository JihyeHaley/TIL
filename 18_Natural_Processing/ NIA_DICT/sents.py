###############################################################
######sentence
# sentence 처음쓰기 새로쓰기
# def raw_sents_input_new():
#     start = str(input('처음 쓰는거 맞으세요? \n\t맞으면 1, \n\t아니면 0을 입력하세요. '))
#     # 처음쓰는 거 아님 (데이터 insert를 방지위해서)
#     if start == '0':
#         return print('append하기 위해서 코드 수정하고 실행시켜주세요!.')
#     # 처음쓰는 거
#     elif start == '1':
#         topic = str(input('어떤 주제인가요?  '))
#         n = int(input(f'{topic}에 관련된 문장을 몇번 입력 받으실래요? '))
#         print('입력을 멈추실려면 0을 눌러주세요')
#         new_sents_log = open(f'/Users/jihyeoh/Desktop/NIA_NER/ NIA_DICT/{topic}_raw_input.txt', 'w')
#         print('새롭게 파일을 생성했습니다.')
#         for i in range(n):
#             if i == 0:
#                 print(f'sample로 {n}개만 먼저 input받습니다.')
#             print(f'{str(i+1)}/{n}개')
#             a = str(input('Input your sent: '))
#             if a == '0':
#                 break
#             sentence = a + '\n'
#             new_sents_log.write(sentence)
#         new_sents_log.close()  


def raw_sents_input_append():
    topic = str(input('어떤 주제인가요?  '))
    n = int(input(f'{topic}에 관련된 문장을 몇번 입력 받으실래요? '))
    print('입력을 멈추실려면 0을 눌러주세요')
    append_sent_log = open(f'/Users/jihyeoh/Desktop/NIA_NER/ NIA_DICT/{topic}_raw_input.txt', 'a')
    
    for i in range(n):
        print(f'{str(i+1)}/{n}개')
        a = str(input('Input your sent: '))
        if a == '0':
            break
        sentence = a + '\n'
        append_sent_log.write(sentence)
    append_sent_log.close() 


