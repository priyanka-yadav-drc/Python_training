s = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
print(s)
result=dict()
result={x:y for x,y in s.items() if y[0] >=5.5 and y[1] >=68}
print(result)