star = 5
begin = 1
space = star - 1

while begin <= star:
    print(' '*space, end='')
    print('*'*begin)
    space, begin = space - 1 , begin + 1