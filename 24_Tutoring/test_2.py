from datetime import datetime

test_dict = {
'당신의 어머니가 언제 도시에 오시죠?':'When is your mother coming into town?',
'왜 Mrs. Cheng이 일찍 떠났죠?':'Why did Mrs. Cheng leave early?',
'멕시칸 레스토랑에서 점심을 주문 하시길 원하죠? 아니요, 오늘은 점심 싸 왔어요.':'Do you want to order lunch from the Mexican restaurant?',
'버스 타실 건가요, 제가 집에 태워드릴까요?':'Are you taking a bus or can I give you a ride home?',
'재킷이 어제 더 비싸지 않았나요?':' Wasn’t this jacket more expensive yesterday?',
'여기서 얼마 동안 일해오고 있죠?':'How long have you been working here?',
'한 시간 전에 여기 오시기로 되어 있었잖아요.':'You were supposed to be here an hour ago.',
'호텔 일자리에 응시해볼 생각이었나요?':'Did you consider applying for a job at the hotel?',
'Joseph이 언제 휴가에서 돌아오죠?':'When will Joseph be returning from his vacation?',
'그녀의 비행기가 두 시간 늦었죠?':'Her plane is two hours late, isn\’t it?',
'어떤 약을 추천하세요?':'Which medicine do you recommend?',
'오늘 밤 저녁 같이 하시겠어요?':'Why don\’t you join us for dinner tonight? Thanks, but I have other plans.',
'이 기타를 어떻게 치는지 여기 아시는 분 있나요?':'Does anyone know here how to play the guitar?',
'급여를 어디서 받을 수 있나요?':'Where can I pick up the payment?',
'우리가 언제 초대에 응답을 해야 하죠?':'When does the invitation say we need to respond?',
'커피 한잔 더 드릴까요?':'Would you like me to get you another cup of coffee?',
'회의가 몇 시에 시작될 예정이죠?':' What time is the conference supposed to begin?',
'Mr. Lee는 집에서 하는 사업이 있지?':'Mr. Lee has a family business, doesn\’t he?',
'이야기 할 시간 있어 아니면 Mr. Navara에게 가 봐야 하니?':'Do you have time to talk or does Mr. Navara need you?'
}

def test():
    timestamp = datetime.now().strftime("%m%d%H%M")
    cnt = 1
    pass_cnt = 0
    fail_cnt = 0
    len_test = len(test_dict)
    test_result = open(f'./test_1_45_' + timestamp +'.txt', "w+")
    for ko, en in test_dict.items():
        # 질문
        question = f'\nQ.{cnt} : {ko}'
        print(question)

        # 정답
        a = str(input())
        answer = f'\t{question} ----\t{en}'
        if a == 'pass':
            test_result.write('Pass' + answer)
            pass_cnt += 1
        elif a == 'fail':
            test_result.write('Fail' + answer)
            fail_cnt += 1

        print(f'A.{cnt} : {en}')
        print(f'pass: {pass_cnt}, fail: {fail_cnt} / total:{len_test}')
        n = str(input())
        if n == ' ':
            cnt += 1
            print('-'*30)
            continue

    result = f'\npass: {pass_cnt}, fail: {fail_cnt} / total:{len_test}'
    test_result.write(timestamp + result)
    test_result.close()

def let_begin():
    print('If you are ready to take exam, please input \'start\'.')
    start = str(input())
    if start == 'start':
        test()
        
    
let_begin()
