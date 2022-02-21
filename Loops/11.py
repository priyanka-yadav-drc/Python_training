row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
matrix=[[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
	for col in range(col_num):
		matrix[row][col]=row*col


for row in range(row_num):
	for col in range(col_num):
		print matrix[row][col], 
	print ''