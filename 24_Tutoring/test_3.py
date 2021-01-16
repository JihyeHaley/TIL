from datetime import datetime
import xlsxwriter

test_dict = {
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
workbook = xlsxwriter.Workbook('./test_3_101_120'  + timestamp +'.xlsx') 
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
