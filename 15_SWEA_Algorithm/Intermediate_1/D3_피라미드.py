#그냥 피라미드
def evenTop():
    # N, X = input().split(' ')
    M = int(input())
    for i in range(1, M + 1):
        print(' '*(M-i)+'X'*(2*i-1),)
# print(list(range(4-1,-1,-1)))
evenTop()