lis=[7,4,2,6,9,0,-1,2]
min=lis[0]
for i in range(len(lis)):
	if lis[i]>min:
		min=lis[i] 
		j=i

new_lis=lis
lis.pop(j)
print(lis)

min=lis[0]
for i in range(len(lis)):
	if lis[i]>min:
		min=lis[i] 

print("second largest element: {}".format(min))