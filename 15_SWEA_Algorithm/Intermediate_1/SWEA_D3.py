# T = int(input())
small = [chr(x) for x in range(65, 91)]
large = [chr(x) for x in range(97, 113)]

def name():
    n = int(input())
    s = str(input()).split(' ')
    start = 0
    result = []
    for i in range(0, len(s)):
        word_len = len(s[i]) - 1 
        result_cnt = 0
        comma = ''
        if s[i][word_len] == '!' or '?' or'.':
            if s[i][word_len] == '!':
                comma = '!'
            elif s[i][word_len] == '?':
                comma = '?'
            elif s[i][word_len] == '.':
                comma = '.'

            s[i][word_len].lstrip(comma)
            section = s[start:i+1]
            print(section)
            for j in range(0, len(section)):
                if section[j][0] in large:
                    small_cnt = 0
                    for k in range(1, len(section)):
                        if section[j][k] in small:
                            small_cnt += 1
                    if small_cnt ==  len(section) - 1:
                        result_cnt += 1
            result.append(result_cnt)

    for i in range(0, len(result)):
        print(f'{result[i]}')


name()