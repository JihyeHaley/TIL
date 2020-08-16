string = 'ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC'
def MapAndLambda():
    score_a = list(map(lambda x:x == 'A', string))
    score_b = list(map(lambda x:x == 'B', string))
    score_c = list(map(lambda x:x == 'C', string))
    score_d = list(map(lambda x:x == 'D', string))
    total = {'a':0, 'b':0, 'c':0, 'd':0}
    
    for i in range(0, len(score_a)):
        if score_a[i] == True:
            total['a'] += 1
        if score_b[i] == True:
            total['b'] += 1
        if score_c[i] == True:
            total['c'] += 1
        if score_d[i] == True:
            total['d'] += 1

    print(total['a']*4+total['b']*3+total['d']*2+total['d']*1)
    
MapAndLambda()
