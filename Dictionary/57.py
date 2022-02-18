dict1={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}

result={}

result={x:[d for d in y if d%2==0] for x,y in dict1.items()}

print(result)