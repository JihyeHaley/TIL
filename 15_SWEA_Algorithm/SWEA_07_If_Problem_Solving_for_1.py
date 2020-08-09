
score = [88, 30, 61, 55, 95]
result = []

for i in range(0, len(score)):
    if score[i] >= 60:
        result.append('합격')
    else:
        result.append('불합격')

for i in range(0, 5):
    print('{0}번 학생은 {1}점으로 {2}입니다.' .format(i+1, score[i], result[i]))