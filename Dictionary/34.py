dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}

result=sum(map(len,dict.values()))
print(result)