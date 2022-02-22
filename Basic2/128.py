def func(txt):
	vow=['a','e','i','o','u']
	return ''.join([x for x in txt if x not in vow])

print(func("Python"))
print(func("Priyanka"))