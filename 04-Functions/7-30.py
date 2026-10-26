def sum_natural(n):
    if n == 1:
        return 1
    return n + sum_natural(n-1)

for n in range(1,11):
    print(f"{n}: sum = {sum_natural(n)}")