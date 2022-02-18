from itertools import combinations

l1=[12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83]
n=3

result = list((l1[i:i+n] for i in range(0, len(l1), n)))
print(result)