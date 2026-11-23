def f():
    a1 = [4,36,12,28,9,44,5] 
    a2 = [5,1,36]
    return [i for i in a1 if i not in a2]

    
print(f())