

def func(lis,li2):
	for x in lis:
		for y in lis2:
			if x==y:
				return True
	return False

lis=[7,2,9,1,0]
lis2=[3,4,5,]
print(func(lis,lis2))