matrix1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
matrix2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
print(matrix1)
print(matrix2)
matrix1.sort(key=sum)
matrix2.sort(key=sum)
print("after sorting: ")
print(matrix1)
print(matrix2)