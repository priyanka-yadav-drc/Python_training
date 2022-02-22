def func(str1):
    return len(str1) == len(set(str1.lower()))


print(func("Priyanka"))
print(func("Python"))
