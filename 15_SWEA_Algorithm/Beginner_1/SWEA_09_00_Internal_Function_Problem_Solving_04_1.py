string = 'ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC'
def MapAndLambda():
    score_a = list(map(lambda x:x == 'A', string))
    score_b = list(map(lambda x:x == 'B', string))
    score_c = list(map(lambda x:x == 'C', string))
    score_d = list(map(lambda x:x == 'D', string))
    total_a = 0
    total_b = 0
    total_c = 0
    total_d = 0

    for i in range(0, len(score_a)):
        if score_a[i] == True:
            total_a += 1
        if score_b[i] == True:
            total_b += 1
        if score_c[i] == True:
            total_c += 1
        if score_d[i] == True:
            total_d += 1

    print(total_a*4+total_b*3+total_c*2+total_d*1)
    
MapAndLambda()
