T = int(input())

def name(T):
    split = []
    for i in range(0, T):
        # 문장의 수 
        n = int(input())
        sentence = str(input())
        split.append(sentence.split('.'))
        split.append(sentence.split('!'))
        split.append(sentence.split('?'))