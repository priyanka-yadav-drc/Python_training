dictt = {'a':5, 'b':14, 'c': 32, 'd':35, 'e':24, 'f': 100, 'g':57, 'h':8, 'i': 100}
n=input("enter n: ")
result=sorted(dictt, key=dictt.get, reverse=True)[:n]
print(dictt)
print(result)