d={'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}

result=[x for x,y in d.items() if y>19]

print(result)