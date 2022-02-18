list1 = [[1], [4],[5, 7], [9, 11], [13, 15, 17]] 
max_length = max(len(x) for x in list1 )
max_list = max(list1, key = len)
print("Max list with size: ")
print("{}, {}".format(max_length,max_list))

min_length = min(len(x) for x in list1 )
min_list = min(list1, key = len)
print("Min list with size: ")
print("{}, {}".format(min_length,min_list))