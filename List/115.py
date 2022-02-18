list1=[1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
flag=0
for x in list1:
	if list1.count(x)>1:
		flag=1
		break
if flag==1:
	print("list is not unique")
else:
	print("list is unique")