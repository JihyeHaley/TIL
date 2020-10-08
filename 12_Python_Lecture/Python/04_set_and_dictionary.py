############################### sequence가 아닌 ################################
##############################################################################

 # 1. set
print('---- set ----')
set_a = {1, 2, 3}
set_b = {3, 6, 9}
print(set_a - set_b) #차집합
print(set_a | set_b) #합집합
print(set_a & set_b) #교집합

set_c = set() #set은 class를 통해서 선언을 해주고 사용해야 한다. 

#2. dictionary
print('---- dictionary ----')
dict_a = {1: 1, 2: 2, 3: 3} #set이랑 똑같이 생겼는데 기본값은 dictionary
#key가 겹쳐버리면 나중에 씌인 값이 나온다.
print(dict_a)
print(type(dict_a))
dict_b = dict()
print(type(dict_b))

print('\n---- dictionary read ----')
a = 서울
phone_book={
    a : '02',
    '경기' : '031'
}

print(phone_book['서울']) #접근은 대괄호로
print(phone_book[a]) #접근은 대괄호로

print('---dir 함수 사용해서 뭔가 볼 수 있다.---')

print(dir( dict))

print(phone_book.values())

#dict_values로 출력되는데 뭘까요?? -> 감싸고 있는 대괄호를 보고 list로 보면 된다~~!
#print(help(dict)) # 다 외우지는 않는다.