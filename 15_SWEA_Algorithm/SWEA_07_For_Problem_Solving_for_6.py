bt = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
result = {'A':0, 'O':0, 'B':0, 'AB':0}

for i in range(0, len(bt)):
    if bt[i] == 'A':
        result['A'] = result['A']+ 1
    elif bt[i] == 'O':
        result['O'] = result['O']+ 1
    elif bt[i] == 'B':
        result['B'] = result['B']+ 1
    elif bt[i] == 'AB':
        result['AB'] = result['AB']+ 1

print(result)
