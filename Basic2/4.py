def func(lis):
	for i in range(len(lis)):
		for j in range(len(lis)):
			for k in range(len(lis)):
				if i!=j and j!=k and i!=k:
					if lis[i]+lis[j]+lis[k]==0:
						
						print(lis[i],lis[j],lis[k])


lis=[-6,3,9,-8,-1,3,5,2]
func(lis)