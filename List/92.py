list1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]] 
list2 = [[1, 3],[13,15,18]] 
print(all(map(list1.__contains__, list2)))