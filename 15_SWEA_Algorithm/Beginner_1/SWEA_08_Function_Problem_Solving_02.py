def game():
    man = input() 
    man += input() 
    game = input()
    game += input()
    
    if '가위' and '바위' in game:
        print('바위가 이겼습니다!')
    elif '바위' and '보' in game:
        print('가위가 이겼습니다!')
    elif '가위' and '보' in game:
        print('보자기가 이겼습니다!')

game()