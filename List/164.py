l1=[12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83]
n=sum(1 for i in l1 if (i> 45 and i % 2 == 0))
print(n)