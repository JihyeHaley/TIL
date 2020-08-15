def length():
    a, b = input().split()
    compare1 = str(a[0])
    compare2 = str(b)
    
    
    if len(compare1) >= len(compare2):
        print(compare1)
    else:
        print(compare2)
length()