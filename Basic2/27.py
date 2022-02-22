def func(ar):
	if ar[0]==ar[1]==ar[2]:
		print("It is neither AP not GP")
	elif ar[1]-ar[0]==ar[2]-ar[1]:
		print("It is AP")
		print("Next number={}".format(ar[2]+(ar[2]-ar[1])))
	else:
		print("It is GP")
		print("Next number={}".format(ar[2]**2/ar[1]))

func([1,2,3])
func([2,4,8])