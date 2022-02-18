import itertools      
d ={'1':['a','b'], '2':['c','d']}
for combo in itertools.product(*[d[k] for k in d.keys()]):
    print(''.join(combo))
	
