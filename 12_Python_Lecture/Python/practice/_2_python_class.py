class Dog1:
    kind = 'canine'

    def __init__(self, name):
        self.name = name

print('----Dog1----')
my_dog = Dog1('ccobi')
your_dog = Dog1('happy')

print(my_dog.kind)
#canine
print(your_dog.kind)
#canine
print(my_dog.name)
#ccobi
print(your_dog.name)
#happy

class Dog2:
    tricks = []

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

print('----Dog2----')

my_dog2 = Dog2('ccobi')
your_dog2 = Dog2('happy')

my_dog2.add_trick('hello')
print(my_dog2.tricks)
#hello

your_dog2.add_trick('hihi')
print(your_dog2.tricks)
#hello,hihi

print(my_dog2)
#object객체
print(your_dog2)
#object객체

print(my_dog2.name)
#ccobi
print(your_dog2.name)
#happy

#hello

#hello, hihi ????


class Dog3:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

print('----Dog3----')
my_dog3 = Dog3('ccobi')
your_dog3 = Dog3('happy')

my_dog3.add_trick('hello')
your_dog3.add_trick('hihi')

print(my_dog3.tricks)
#hello, hihi

#hello, hihi
print('''
Dog2 와 Dog3 의 차이점
클래스 안에 trick = []이 존재하는게 아님.
''')
print(my_dog3.name)
print(your_dog3.name)

variable = 'apple'
print(variable.capitalize())
print(str.capitalize(variable))


print('----절차지향----')
def greeting(name):
    return f'hello, {name}'

print(greeting('jihye'))

print('----객체지향----')
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'hello, {self.name}'
print('''class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'hello, \{self.name\}'
를 작성하고
my_name = Person('jihye')
print(my_name.greeting())
를 돌려볼까요?
결과는...''')
my_name = Person('jihye')
print(my_name.greeting())
print('이렇듯...')