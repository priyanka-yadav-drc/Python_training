row=input("Enter number of rows: ")
column=input("Enter number of columns: ")

matrix=[]
print("enter numbers rowwise: ")

for i in range(row):
	a=[]
	for j in range(column):
		a.append(input())
	matrix.append(a)

for i in range(row):
	for j in range(column):
		print(matrix[i][j]),
	print("\n")

sum = [0]*column
print("sum for each column:")
for columns in range(column):
    for rows in range(row):
        sum[columns] += matrix[rows][columns]
    print(sum[columns])
