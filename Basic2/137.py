def func(str1, str2):
    for i in range(len(str2)):
        while str2[i:] in str1 and str2[-1]==str1[-1]:
            return str2[i:]
    return ""

print(func('running','walking'))