n=input("Enter how many numbers you want to enter: ")
a=[]
print("input numbers: ")
for i in range(n):
	a.append(input())
sum=0
for x in a:
	sum+=x

print("Maximum sum of the said contiguous subsequence: {}".format(sum))
