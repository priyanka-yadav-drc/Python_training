l1=[1, 2, 3, 4, 5, 6, 7, 8]
l2=[2, 2, 3, 1, 2, 6, 7, 9]
l3=[2, 1, 3, 1, 2, 6, 7, 9]
result = []
count=0
for m, n, o in zip(l1, l2, l3):
        if (m == n == o):
            result.append(m)
            count+=1

print(count)
print(result)