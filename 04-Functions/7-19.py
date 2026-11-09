def f(number):
    s = str(number)
    total = 0
    for ch in s:
        if s.count(ch) > 1:
            total += int(ch)
    return total

print(f(1027))
print(f(230335))
print(f(513553007))
