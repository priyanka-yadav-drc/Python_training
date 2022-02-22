x = [10, 20, 20, 20]
y = [10, 20, 30, 40]
z = [10, 30, 40, 20]
target=70
for X in x:
	for Y in y:
		for Z in z:
			if (X+Y+Z)==target:
				print(X,Y,Z)