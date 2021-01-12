from datetime import datetime
import xlsxwriter

test_dict = {
'방문객들을 위해 어떤 호텔을 예약해야 하나요?' : ' Which hotel should I reserve for our visitors?',
'왜 파티에 Jennifer의 선물을 가지고 오지 않았니?' : 'Why didn’t you bring Jennifer’s gift to the party?',
'오늘 밤은 한국 음식 먹고 싶어.' : 'I’m in the mood for Korean food tonight.',
'배송이 얼마나 걸리나요?' : 'How long does shipping take?',
'비가 오면 환불 해주지?' : 'They’ll refund our money if it rains, right?',
'난 네가 어제 파리로 떠난 줄 알았어.' : ' I thought you left for Paris yesterday.',
'주문 하실 준비가 되셨어요 아니면 시간이 좀 더 필요하세요?' : 'Are you ready to order or do you need a few more minutes?',
'Mr. Johnson이 구매자에게 전화 하는 것을 내일까지 기다릴 수 있나요?' : 'Can’t Mr. Johnson wait until tomorrow to call the buyer?',
'왜 Ms. Cruise가 2개 국어를 말하는 비서를 고용했죠?' : 'Why did Ms. Cruise hire a bilingual secretary?',
'Mark가 회의에서 발표를 잘했죠?' : 'Mark gave a great presentation at the conference, didn’t he?',
'나중에 커피 마실 시간 있어요?' : 'Are you free for coffee later?',
'그럼 빨리 서둘러야겠군요.' : 'We’d better hurry then.',
'스웨터를 입는 게 어때?' : 'Why don’t you get your sweater?',
'Ms. Jao, 잡지를 어떻게 판촉을 할 건지 말해 주시겠어요?' : 'Ms. Jao, could you tell us how you’d promote the magazine?',
'당신의 여정을 받으시는 대로 전화를 주세요.' : 'Please call me when you have your itinerary.',
'제 사무실을 찾으시는데 문제가 있으셨나요?' : 'Did you have any trouble finding my office?',
'이번 주 일기 예보가 어때요?' : 'What’s the weather forecast for this week?',
'막 문을 연 극장 좋아하세요?' : 'Do you like the theater that just opened?',
'Ms. Johns에게 누가 전화 왔다고 전해 드릴까요?' : 'Can I tell Ms. Johns who is calling?',
'신체 검사 결과를 언제 받을 수 있나요?' : 'When can I get results of my physical?',
'싱가포르에 오신 목적이 무엇입니까?' : 'What is the purpose of your visit Singapore, sir?',
'신용 카드로 낼 수 있나요 아니면 현금으로 내야 하나요?' : 'CanIpaybycreditcard,ordoIhavetopaycash?',
'누가 부매니저로 고용이 되었죠?' : ' I wonder who will be hired as an assistant manager, don’t you?',
'오늘 공연의 표가 있나요?' : 'Are there any tickets available for today’s show?',
'기차역에서 호텔이 얼마나 머나요?' : 'How far is the hotel from the train station?',
'워크샾에 충분한 설문조사지가 있었나요?' : ' Were there enough questionnaires for the workshop?',
'어디서 커피를 살 수 있는지 아세요?' : 'Do you know where I can get a cup of coffee?',
'일 끝난 후 테니스 치실래요?' : 'Do you feel like playing tennis after work?',
'아침 내내 시간 있으시죠?' : 'You are going to be free all morning, aren’t you?',
'이 지역에 좋은 식당 추천해 주시겠어요?' : 'Could you recommend any good restaurants in the area?',
'그냥 안내 센터로 전화를 걸어 볼 수 없을까?' : 'Couldn’t we just call the information line?',
'바깥에 공사가 소음이 너무 심해요.' : 'That construction work outside is making so much noise.',
'파티를 위해 다과를 주문할 필요가 있지 않나요?' : 'Don’t you need to order refreshments for the party?',
'며칠 휴가 내서 쉬는 게 어때?' : 'Why don’t you take a few days off and get some rests?',
'복사기 지금 사용할 필요 없죠?' : 'You don’t need to use the copier now, do you?',
'실험실 비품들이 왜 늦는지 Mr. Davidson가 물어보지 않던가요?' : 'Did Mr. Davidson ask why the shipment of laboratory supplies was late?',
'연구 프로젝트 팀을 이끄시겠어요 아니면 혼자 일하시겠어요?' : 'Would you rather lead the research project team, or work independently?',
'급여 지급을 담당하고 있는 사람이 누구죠?' : 'Who is the person in charge of payroll?',
'읽을책을가지고가고싶지않니?' : 'Don’t you want to bring a book to read?',
'런던으로 언제 가실 겁니까?' : 'When do you leave for London?',
'우산을 어디서 살수있죠?' : 'Where can I buy an umbrella?',
'강연이 지루하지 않았나요?' : 'Didn’t you think the talk was boring?',
'Bill의 전화를 언제 회신 했는지 기억해?' : 'Do you remember when I returned Bill’s call?',
'대신에 이 신발 신어보시겠어요?' : 'Would you like to try these shoes on instead?',
'표를 언제 가지러 가셨나요?' : 'When did you pick up the tickets?',
'차에 설탕 아니면 꿀을 넣으시겠어요?' : 'Would you rather have sugar or honey with your tea?',
'매일 아침 왜 그렇게 일찍 오세요?' : 'Why do you come to work so early every morning?',
'어떻게 그렇게 빨리 프로젝트를 끝낼 수 있었죠?' : 'How did you finish the project so quickly?',
'회의를 위해 누가 테이블과 의자를 정돈 할 예정인가요?' : 'Who’s going to set up the tables and chairs for the conference?',
'세금 보고서가 곧 마감 아닌가요?' : 'Aren’t the tax forms due soon?',
'비행기가세시이후에온다면반나절을쉬셔야할것 같아요.' : ' If your plane comes in after three, I think you should take the rest of day off.',
'회의를 위해 누가 테이블과 의자를 정돈 할 예정인가요?' : 'Who’s going to set up the tables and chairs for the conference?',
'세금 보고서가 곧 마감 아닌가요?' : 'Aren’t the tax forms due soon?',
'Ms. Decathy가 오늘 아침 회의를 소집한 이유를 아세요?' : 'Do you know why Ms. Decathy is calling this morning’s meeting?',
'회의가 끝난 후에 저녁 드시러 나가시겠어요?' : 'Would you like to go out for dinner after the meeting?',
'이런 더운 날씨가 싫어요.' : ' I don’t like this hot weather.',
'Carol이 없는 동안 누가 그 자리를 대신 할 지 아세요?' : 'Do you know who will be replacing Carol while she’s away?',
'Mary가 회계부에 송장을 보내야 되죠?' : 'Mary needs to send her invoice to accounting, doesn’t she?',
'고용한 새 기술자는 일에 적응되고 있나요?' : 'Is the new engineer we hired getting used to the job?',
'계약서를 보내 드릴까요 아니면 가지러 오시겠어요?' : 'Should I have the contract sent to you or will you pick it up?',
'지난 주 판매 수치를 막 업데이트했죠?' : 'We just updated those sales figures last week, didn’t we?',
'신청서를 진행시키는 가장 빠른 방법이 있나요?' : 'Is there a faster way to process applications?',
'왜 Peter이 내일 저녁 근무를 원하죠?' : 'Why does Peter want to work the evening shift tomorrow?',
'Mr. Chan이 은퇴를 할 때 어떻게 경의를 표할 수 있을까?' : 'How should we honor Mr. Chan when he retires?',
'How about shipping the materials this afternoon?' : '오늘 오후에 재료를 보내는게 어때?'
}


# excel idx 
def _excel_index_creator(colum, row_idx):
    colum_idx = colum + str(row_idx)
    return colum_idx

# timestamp
timestamp = datetime.now().strftime('%m%d%H%M')

# Open and create each excel file
workbook = xlsxwriter.Workbook('./test_2_46_120'  + timestamp +'.xlsx') 
worksheet = workbook.add_worksheet()

# Column Color
cell_red = workbook.add_format()
cell_red.set_pattern(1)
cell_red.set_bg_color('red')
cell_blue = workbook.add_format()
cell_blue.set_pattern(1)
cell_blue.set_bg_color('blue')


worksheet.write('A2', 'no')
worksheet.write('B2', 'P/F')
worksheet.write('C2', 'Ko')
worksheet.write('D2', 'En')



def test():
    cnt = 1
    pass_cnt = 0
    fail_cnt = 0
    len_test = len(test_dict)
    row_idx = 3

    # questions start
    for ko, en in test_dict.items():
        a_idx = _excel_index_creator('A', row_idx)
        b_idx = _excel_index_creator('B', row_idx)
        c_idx = _excel_index_creator('C', row_idx)
        d_idx = _excel_index_creator('D', row_idx)

        # a - idx
        worksheet.write(a_idx, str(cnt))
        # c - ko
        worksheet.write(c_idx, str(ko))
        # d - en
        worksheet.write(d_idx, str(en))

        # 질문 출력
        question = f'\nQ.{cnt} : {ko}' 
        print(question)

        # 정답
        a = str(input())
        if a == 'p':
            worksheet.write(b_idx, 'P', cell_blue)
            pass_cnt += 1
        elif a == 'f':
            worksheet.write(b_idx, 'F', cell_red)
            fail_cnt += 1

        print(f'A.{cnt} : {en}')
        print(f'pass: {pass_cnt}, fail: {fail_cnt} / total:{len_test}')

        row_idx += 1

        n = str(input())
        if n == ' ':
            cnt += 1
            print('-'*30)
            continue
    
    # 전체 개수 적기
    pass_cnt = f'p: {pass_cnt}'
    fail_cnt = f'f: {fail_cnt}'
    worksheet.write('A1', '결과')
    worksheet.write('B1', str(pass_cnt), cell_blue)
    worksheet.write('C1', str(fail_cnt), cell_red)
    workbook.close()

def let_begin():
    print('If you are ready to take exam, please input \'start\'.')
    start = str(input())
    if start == 'start':
        test()
        
    
let_begin()
