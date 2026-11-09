def f(expression):
    total = int(expression[0])
    for i in range(1, len(expression), 2):
        op = expression[i]
        num = int(expression[i + 1])
        if op == "+":
            total += num
        elif op == "-":
            total -= num
    return total

print(f("2+3"))
print(f("3+8+1"))
print(f("2+3-4+5-0"))
