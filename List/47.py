color = ['Red', 'Green', 'Black']
print(color)
new=[x for y in color for x in ('*', y) ]
print(new)