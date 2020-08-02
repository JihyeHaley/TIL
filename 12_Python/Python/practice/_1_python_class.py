class Dog1:
    kind = 'canine'

    def __init__(self, name):
        self.name = name

print('--dog1--')
my_dog = Dog1('gazi')
your_dog = Dog1('namu')

print(my_dog.kind)
print(your_dog.kind)
print(my_dog.name)
print(your_dog.name)

class Dog2:
    tricks = []

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

print('--dog2--')
my_dog = Dog2('gazi')
your_dog = Dog2('namu')

my_dog.add_trick('hello')
my_dog.add_trick('hihi')

print(my_dog)
print(my_dog.name)
print(your_dog.name)
print(my_dog.tricks)
print(your_dog.tricks)

class Dog3:
    def  __init__(self, name):
        self.name = name
        self.tricks = [] #인스턴스 변수가 각각 가져오고 싶으면 인스턴스 안에 넣어야 한다.

    def add_trick(self, trick):
        self.tricks.append(trick)

print('--dog3--')
my_dog = Dog3('gazi')
your_dog = Dog3('namu')

my_dog.add_trick('hello')
your_dog.add_trick('hihi')

#클래스변수는 모든 인스턴스가 참조한다.
print(my_dog.tricks)
print(your_dog.tricks)
print(my_dog.name)
print(your_dog.name)

variable = "apple"
print(variable.capitalize())
print(str.capitalize(variable))

# 절차 지향 vs 객체지향
# 데이터가 흘러 다니느 것으로 보는 시간 -> 데이터가 중심이 되는 시각

# 절차 지향
# greeting(데이터)
def greeting(name):
    return f'hello, {name}'

print(greeting('jihye'))

# 객체지향 
# 데이터. greeting()
class person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'hello, {self.name}'

print('----class person----')
my_name = person('jihye')
print(my_name.greeting())

class Hello:
    def __init__(self, name):
        self.name = name
    
    def sayHi(self):
        return f'hello, {self.name}'

print('----class Hello----')
my_name2 = Hello('JIHYE')
print(my_name2.sayHi())

class HiHello:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        return f'hello, this is {self.name}'

print('----HiHello----')
my_word = HiHello('jihyeoh')
print(my_word.sayHi())


