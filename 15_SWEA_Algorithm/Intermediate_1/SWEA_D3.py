T = int(input())

def name(T):
    split = []
    comma = 'last'
    for i in range(0, T):
        n = int(input())
        sentence = str(input())
        split.append(sentence.split(' '))
        for j in range(0, len(split)):
            word_len = len(split[i]) - 1 
            if split[j][word_len] == '!':
                comma = '!'
            elif split[j][word_len] == '.':
                comma = '.'
            elif split[j][word_len] == '?':
                comma = '?'
            else:
                pass
                
            if split[i][word_len] == '!' or '?' or '.':
                split.append(sentence.split())