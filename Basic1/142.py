def test(str1):
    while '01' in str1:
        str1 = str1.replace('01', '')
    return len(str1) == 0

print(test("0101"))
print(test("001"))