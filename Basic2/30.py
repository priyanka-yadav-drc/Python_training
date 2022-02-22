def func(n):
	while True:
		k=str(n)

		if k==k[::-1]:
			break
		else:
			m=int(k[::-1])
			n=n+m

	return n

print(func(1234))
print(func(5678))