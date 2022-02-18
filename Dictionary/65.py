lis={'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
sum=0

for k,v in lis.items():
	sum=sum+ len(v)

print(sum)