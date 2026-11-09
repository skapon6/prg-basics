def f(text):
    result = ""
    for i in range(len(text)):
        if i > 0:
            result += "-"
        result += text[i]
    return result

print(f("Univesity"))
print(f("UE"))
print(f("x"))
print(f(""))
