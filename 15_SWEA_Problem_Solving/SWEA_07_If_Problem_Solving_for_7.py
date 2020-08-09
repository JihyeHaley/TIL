score = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
total = 0


while len(score):
    a = score.pop() 
    if a >= 80:
        total = total + a

print(total)