# T = int(input())
small = [chr(x) for x in range(65, 91)]
large = [chr(x) for x in range(97, 113)]

def name():
    # n = int(input())
    s = str(input()).split(' ')
    start = 0
    for i in range(0, len(s)):
        section = []
        result = []
        if s[i][-1] == '!' or '?' or'.':
            print(i, section, s[i][-1])
            section = s[start:i+1]
            start = i+1
            for j in range(0, len(section)):
                result_cnt = 0
                small_cnt = 0
                if section[j][0] in large:
                    for k in range(1, len(section[j])):
                        if section[j][k] in small:
                            small_cnt += 1
                        if small_cnt == len(section[j])-1:
                            result_cnt += 1
                result.append(result_cnt)
    print(result)

name()



