lis=[3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 5, 9, 9, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1]
count=0
previous_digit=0
for digit in lis:
	if previous_digit==0 and digit!=0:
		count+=1
	previous_digit=digit
print(lis)

print(count)
