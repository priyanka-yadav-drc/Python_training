items = [('item2', 10, 10.12), ('item3', 15, 25.10), ('item1', 11, 24.50),('item4', 12, 22.50)]
n=2
result=sorted((items),key=lambda x: x[n])
print(result)