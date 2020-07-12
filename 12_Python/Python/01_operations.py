#논리연산자
# and, or, not
#################and##################
##and는 1개만 false여도 false
print('---- and ----')
print(True and True)
print(True and False)
print(False and True)
print(False and False)

#################or##################
# ctrl + d 로 블럭을 짓고 letter을 바꾸면 한꺼번에 변경될 수 있다.
##or는 1개만 true여도 true
print('---- or ----')
print(True or True)
print(True or False)
print(False or True)
print(False or False)

#################not##################
#### not은 반대가 출력된다.
print('---- not ----')
print(not True)
print(not False)
print(not 0)
print(not {})


#########################단축평가###########################
#단축평가 (결과가 확정됐을 때 뒤쪽의 코드는 읽지 않는다.)
print('---단축평가 and ---')
print("""
첫번째 값이 확실할 때, 두번째 값은 확인하지 않음
조건문에서 뒷 부분을 판단하지 않아도 되기 때문에 속도 향상을 위해서 
""")
# 첫번째 값이 확실할 때, 두번째 값은 확인하지 않음
# 조건문에서 뒷 부분을 판단하지 않아도 되기 때문에 속도 향상을 위해서 
vowels = 'aeiou'
('a' and 'b') in vowels # in 은 어디 안에 있는지 알려주는 것

print(('a' and 'b') in vowels) #false
print(('b' and 'a') in vowels) #true
print('a' and 'b') # -> b , and는 평가를 끝까지 해야지 T or F 값을 알 수 있따. and의 원리를 잘 이해하면 좋을 것 같당!
print('b' and 'a') # -> a

# and는 둘다 True 일 경우에만 True 이기 때문에 
# 첫번째 값이 True 라도 두번째 값을 확인해야 한다.
print(3 and 5) # 5
print(3 and 0) # 0 
print(0 and 3) # 0 (앞의 0이 flase 라서 0이 나온다.)
print(0 and 0) # 0 (왼쪽의 0)


print('----단축평가 or----')

# and는 둘다 True 일 경우에만 True 이기 때문에 
# 첫번째 값이 True 라도 두번째 값을 확인해야 한다.
print(5 or 3) # 5 ( or는 첫번째것이 True 이면 뒤에 볼 필요도 없으니깐 5가 나온다.)
print(3 or 0) # 3 
print(0 or 3) # 3 
print(0 or 0) # 0 (오른쪽 0)

#########################Containment Test###########################
# in 연산자를 통해 요소가 속해있는지 여부를 확인할 수 있다.
print('--- in ---')
print('a' in 'apple')
print(1 in [1, 2, 3]) #list . array이랑 똑같은데 python에서만 list라고 부른다.