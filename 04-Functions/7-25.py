def f(x,y):
    candidate = set()
    result = 0
    for i in range(x,y+1):
        for j in range(x,y+1):
            candidate.add(i+j)
    for digit in candidate:
        if digit % 2 == 0 and digit % 3 == 0 and digit % 4 != 0:
            result = digit
    return result
    
print(f(10,30))
    