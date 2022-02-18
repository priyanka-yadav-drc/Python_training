nums = [
        [1,2,3,2],
        [4,5,6,2],
        [7,8,9,5],
       ] 
result=[]

for x in nums:
	for i in x:
		result.append(i)
print(result)
for x in result:
	print("{}, {}".format(x, result.count(x)))