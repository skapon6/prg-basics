def f():
    t = [34,7,19,4,21,8]
    result = []
    i = 0
    while i < len(t):
        if t[i] % 2 == 0:
            result.append(t[i])
        i+=1
    return result
            
print(f())