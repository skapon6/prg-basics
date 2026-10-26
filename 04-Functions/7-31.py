def power(x,n):
    if n == 1:
        return 1
    
    return x * (x**(n-1))

print(power(5,3))