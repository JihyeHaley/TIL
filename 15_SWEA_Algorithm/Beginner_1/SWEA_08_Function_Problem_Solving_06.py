ordinary = [2, 4, 6, 8, 10]
def check():
    compare = [5, 10]
    result = []
    for i in range(0, 2):
        if compare[i] in ordinary:
            result.append('True')
        elif compare[i] not in ordinary:
            result.append('False')
        
    print(ordinary)
    for j in range(0, 2):
        print(f'{compare[j]} => {result[j]}')

check()
