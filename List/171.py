l1 = ['0','1','2','3','4'] 
l2 = ['red','green','black','blue','white']
l3 = ['100','200','300','400','500'] 
result=[i + j + k for i, j, k in zip(l1, l2, l3)]
print(result)