x1=['S001', 'S002', 'S003', 'S004']
y1=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
z1=[85, 98, 89, 92]

dict1=dict()

dict1={x:{y:z} for x,y,z in zip(x1,y1,z1)}
print(dict1)