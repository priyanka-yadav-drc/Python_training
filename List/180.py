lst=[3,2,0,9,8,50]
result = ''.join(sorted((str(val) for val in lst), reverse=False) )
	#key=lambda i: i*( len(str(min(lst))) * 2 // len(i))))

print(result)