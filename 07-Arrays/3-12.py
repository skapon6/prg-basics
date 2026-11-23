def f(a : list):
    return [i for i in a if a.count(i) <2]

print(f([2,3,2,5,8,1,9,8]))