lst=['abc ', '  ', ' ', 'sdfds ', ' ', '     ', 'sdfds ', 'huy']

result =[]
for i in lst:
        j = i.replace(' ','')
        result.append(j)

print(result)