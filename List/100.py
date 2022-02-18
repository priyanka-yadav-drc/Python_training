l1 = [1, 1, 3, 4, 5, 6, 7, 8]
l2 = [0, 1, 2, 3, 4, 8, 7, 8]
l3 = [0, 1, 2, 3, 4, 5, 7, 8]


result = []
for m, n, o in zip(l1, l2, l3):
        if (m == n == o):
            result.append(m)

print(result)