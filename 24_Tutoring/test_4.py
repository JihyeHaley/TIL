from datetime import datetime
import xlsxwriter

test_dict = {
'Snowman 신문사에 이 자리가 있었는지 어떻게 아셨죠?':'How did you learn of this position at Snowman Press?',
'해변에 같이 가시겠어요?':'Why don’t you come to the beach with us?',
'디자인 프로젝트 작업을 누가 할 예정인가요?':'Who is going to be working on the design project?',
'경주가 언제 시작될 거죠?':'When is the race supposed to start?',
'Mr. Williams가 조금 늦지 않았나요?':' Isn’t Mr. Williams a little late?',
'서류 캐비닛의 열쇠가 어떤 건가요?':'Which is the key to the filing cabinet?',
'왜 일정이 변경되었나?':' Why was the schedule changed?',
'두 시에 만나기로 되어있지 않았나요?':' Weren’t we supposed to meet at two?',
'제가 빌려드린 책 다 읽으셨어요?':'Have you finished the book I lent you?',
'회의실이 얼마나 큰가요?':'ow big is the meeting room?',
'참고 서적이 누구의 것인가요?':'Who does this reference manual belong to?',
}


# excel idx 
def _excel_index_creator(colum, row_idx):
    colum_idx = colum + str(row_idx)
    return colum_idx

# timestamp
timestamp = datetime.now().strftime('%m%d%H%M')

# Open and create each excel file
workbook = xlsxwriter.Workbook('./test_4_121_140'  + timestamp +'.xlsx') 
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
