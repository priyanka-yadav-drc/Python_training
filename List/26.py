list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]

print("comparing list 1 and list 2: ")
print(''.join(map(str,list1)) in ''.join(map(str,list2*2)))
print("comparing list 2 and list 3: ")
print(''.join(map(str,list2)) in ''.join(map(str,list3*2)))