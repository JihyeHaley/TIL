words = ['cat', 'window', 'defenstrate']
for w in words:
    print(w, len(w))

for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)
print(words)


# 
print('''----insert에 대해서----
insert(a, b)
a번째에 b를 추가해라''')