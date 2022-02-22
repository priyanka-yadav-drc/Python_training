def func(lis1,lis2):
	x1,y1,r1=lis1
	x2,y2,r2=lis2

	dist= ((x1-x2)**2 + (y1-y2)**2)**0.5

	if dist<=r1+r2:
		return True
	else:
		return False

print(func([1,2,4],[1,2,8]))
print(func([0,0, 2], [10,10, 5]))