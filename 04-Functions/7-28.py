def f(dice):
    result, _max = dice[0], 0
    for i in range(0,len(dice)):
        c = 1
        for j in range(i+1,len(dice)):
            if dice[i] != dice[j]:
                # print(f"{dice[i]} !== {dice[j]}")
                break
            # print(f"{i}:{dice[i]} == {j}:{dice[j]}")
            c+=1
        if c > _max:
            _max = c
            result = dice[i]
    return result


            