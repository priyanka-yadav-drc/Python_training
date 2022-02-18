l1 = [2, 4, 7, 0, 5, 8]
l2 = [3, 3, -1, 7]

f_len = len(l1)-(len(l2) - 1)
for i in range(len(l1), 0, -1):
        if i-f_len < 0:
            break
        else:
            l1[i-1] = l1[i-1] + l2[i-f_len]
print(l1)