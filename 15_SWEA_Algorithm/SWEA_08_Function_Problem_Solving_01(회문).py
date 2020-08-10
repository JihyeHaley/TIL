word = str(input())
length = len(word)
middle = length//2
result = f'{word}\n입력하신 단어는 회문(Palindrome)입니다.'

def check(word):
    i = 0 # 첫 값
    j = length - 1 # 마지막 값
    
    while i <= middle:
        if word[i] == word[j]:
            i += 1
            j += -1
        elif word[i] != word[j]:
            break
        
        if i == middle:
            print(result)
check(word)


