lis=[{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]

result=[]

result=list(d['Math'] for d in lis)
print(result)