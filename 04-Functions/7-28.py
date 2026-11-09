def f(dice):
    result = dice[0]
    max_count = 0
    for i in range(len(dice)):
        c = 1
        for j in range(i + 1, len(dice)):
            if dice[i] != dice[j]:
                break
            c += 1
        if c > max_count:
            max_count = c
            result = dice[i]
    return int(result)

print(f("5233165554211"))
print(f("2133"))
