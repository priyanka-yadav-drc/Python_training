list1=[1, 1, 3, 4, 4, 5, 6, 7]
list2=[0, 1, 2, 3, 4, 4, 5, 7, 8]

sum=0
l1=len(list1)
l2=len(list2)
l=l1+l2

for x in list1:
	sum=sum+x

for y in list2:
	sum=sum+y

avg=float(sum)/l
print(avg)