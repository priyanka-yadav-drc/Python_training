color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

with open("demo.txt",'w') as f:
	for c in color:
		f.write(c)

content = open('demo.txt')
print(content.read())