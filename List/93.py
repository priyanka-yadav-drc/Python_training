list1 = [[1, 3], [1, 5, 7], [9, 11], [13, 15, 17]] 
count=0
n=input("enter element to find count of: ")
for x in list1:
	if n in x:
		count+=1

print(count)