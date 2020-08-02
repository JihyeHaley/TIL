classroom = {
    'teacher' : 'jihye',
    'student1' : 'ai',
    'student2' : 'design',
}

print(classroom)

# key출력
print('----print value----')
for member in classroom:
    print(member)

# key값으로 접근해서 value 출력
print('----approach with key to print value----')
for member in classroom:
    print(classroom[member])

# dict key 으로 key 출력
print('----dict keys----')
for member in classroom.keys():
    print(member)

# dict value 으로 value 출력
print('----dict values----')
for member in classroom.values():
    print(member)

# dict item 으로 value 출력
print('----dict items (member)----')
print('tuple로 출력됨')
for member in classroom.items():
    print(type(member))

# dict item 으로 value 출력
print('----dict items (key, value)----')
for key, value in classroom.items():
    print(key, value)
    print(type(key))
    print(type(value))