# game = {'가위' : 0, '바위' : 1, '보' : 2}


man1 = str(input())
man2 = str(input())
man1_win = 'Result : Man1 Win!'
man2_win = 'Result : Man2 Win!'
draw = 'Result: Draw'
game = ['가위', '바위', '보']

def game_start(man1, man2):
    if man1 == game[0]:
        if man2 == game[0]:
            print(draw)
        elif man2 == game[1]:
            print(man2_win)
        elif man2 == game[2]:
            print(man1_win)

    elif man1 == game[1]:
        if man2 == game[0]:
            print(man1_win)
        elif man2 == game[1]:
            print(draw)
        elif man2 == game[2]:
            print(man2_win)

    elif man1 == game[2]:
        if man2 == game[0]:
            print(man2_win)
        elif man2 == game[1]:
            print(man1_win)
        elif man2 == game[2]:
            print(draw)

game_start(man1, man2)
