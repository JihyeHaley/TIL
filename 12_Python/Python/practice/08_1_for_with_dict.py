classroom = {
    'teacher' : 'kim',
    'student1' : 'hong',
    'student2' : 'choi',
}


#key
print('----simple_key----')
for member in classroom:
    print(member)

#value
print('----simple_value----')
for member in classroom:
    print(classroom[member])

#key
print('----key----')
for member in classroom.keys():
    print(member)

#value
print('----value----')
for member in classroom.values():
    print(member)

#key, value
print('----key, value----')
for key, value in classroom.items():
    print(key, value)


print('----items 접근----')
print(classroom.keys())
print(classroom.values())
print(classroom.items())