# 피보나치 수열
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
    # print 위에 꺼 해줘

fib(1000)
print(fib(1000))


# 피보나치 수열을 리스트로 만들어서 반환
def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
    

# h = int(input('input a number: '))
# print(fib2(h))

# prompt는 문장이 들어갈 수 있는거고
# retires는 몇 번 반복하고 (0부터 시작) 말 안들으면 error낼지
# 그래서 retries는...-1 을 해주면 입력한 만큼만 작동을한다.
# reminder은 틀렸을때 내보낼 아이
def ask_ok(prompt, retries=4, reminder='please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0 :
            raise ValueError('invalid user response')
        print(reminder)

# ask_ok('정말 끝내길 원하세요?')
# ask_ok('파일을 덮어쓰길 원하세요?', 2 )
# ask_ok('파일을 덮어쓰길 원하세요?', 2 , 'answer only with yes or no')

i = 5 
def f(arg=i):
    print(arg)

i = 6 
print(f(6)) # none 출력됨


def ff(a, L=[]):
    L.append(a)
    return L

print(ff(1))
print(ff(2))
print(ff(3))

def fff(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(fff(5))
print(fff(6))


