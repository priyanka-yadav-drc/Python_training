cars = {'Toyota':{'model':'Glanza',
        'color':'red'},
        'Tata':{'model': 'Nano',
        'color':'white'}}
for a in cars:
    print(a)
    for b in cars[a]:
        print (b,':',cars[a][b])
		