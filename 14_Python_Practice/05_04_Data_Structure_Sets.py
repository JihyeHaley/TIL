# Set
print('''
A set is an unordered collection with `no duplicate elements`
''')

print('''
union, intersection, difference, and symmetric difference.
''')

print('''
need to `set()` in order to create empty set
''')

basket = {'apple', 'ornage', 'apple', 'pear', 'ornage', 'banana'}
# there are two of 'apple' variables
print(basket)

'orange' in basket
'crabgrass' in basket

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a|b)
print(a-b)
print(b-a)
print(a&b)
print(b&a)
print(a^b) # //letter in a or b but not both (without both)

a = {x for x in 'abracadabra' if x not in 'abc'}
print('''
for x in 'abracadabra': # a-5 b-2 c-1 d-1 r-2
    if x not in 'abc' # a,b,c 아닌 것들만 남네
''')

print(a) # {'d', 'r'}