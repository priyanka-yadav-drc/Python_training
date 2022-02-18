t=[[1,2],[8,9]]

flat_list = []
for sublist in t:
    for item in sublist:
        flat_list.append(item)

print(flat_list)