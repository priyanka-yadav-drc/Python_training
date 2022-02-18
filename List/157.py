list1 = [2, 4, 7, 0, 5, 8]
list2 = [2, 5, 8]
list3 = [0, 1]
list4 = [3, 3, -1, 7]

result = []
l1 = len(list1)
l2 = len(list2)
l3 = len(list3)
l4 = len(list4)
    
for i in range(max(l1, l2, l3, l4)):
        if i < l1:
            result.append(list1[i])
        if i < l2:
            result.append(list2[i])
        if i < l3:
            result.append(list3[i])
        if i < l4:
            result.append(list4[i])

print(result)