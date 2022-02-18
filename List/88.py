n=input("enter the size of matrix: ")
matrix=[]
print("enter numbers rowwise: ")

for i in range(n):
	a=[]
	for j in range(n):
		a.append(input())
	matrix.append(a)

sum=0

for i in range(n):
	for j in range(n):
		print(matrix[i][j]),
		if(i==j):
			sum=sum+matrix[i][j]
	print("\n")

print("sum of primary diagonal: ")
print(sum)