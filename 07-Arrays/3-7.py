def f():
    t = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
    return sorted(t, key= lambda x:len(x), reverse=True)[0]

print(f())