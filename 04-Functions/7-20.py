def f(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return num

print(f(1))
print(f(5))
