def prime(n):
	if n==1:
		return False
	elif n==2:
		return True
	else:
		for x in range(2,n/2):
			if n%x==0:
				return False
		return True

print(prime(17))
print(prime(9))