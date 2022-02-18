def largest(*items):
	return(max(items,key=len))

print(largest([1,2],[1,2,3,4],[4,5,6,7,8]))