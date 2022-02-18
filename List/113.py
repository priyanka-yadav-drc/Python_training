list_color = [{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]
result = [dict(e) for e in {tuple(d.items()) for d in list_color}]
print(result)