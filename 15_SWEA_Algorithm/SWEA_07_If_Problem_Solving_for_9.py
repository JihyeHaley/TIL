begin, space = 4, 0

while begin >= 1:
    print(' '*space, end='')
    print('*'*(begin*2-1))
    space = space + 1
    begin = begin - 1