numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
c_o=0
c_e=0
for x in numbers:
	if(x%2==0) :
		c_e+=1
	else:
		c_o+=1

print("even count: {}".format(c_e))
print("odd count: {}".format(c_o))
