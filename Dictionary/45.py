car = {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12 }

x = car.values()

print(x)
print(len(set(x)))
if len(set(x))==1:
	print("all values in the dictionary are same")
else:
	print("all values in the dictionary are not same")