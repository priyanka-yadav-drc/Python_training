lst=[('red', 'green'), ('black', 'white'), ('orange', 'pink')]

result = [("%s "*len(el)%el).strip() for el in lst]
print(result)