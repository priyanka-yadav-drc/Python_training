marks = [(100, 'Math'), (80, 'Math'), (90, 'Math'), (88, 'Science', 89), (90, 'Science', 92)]

result=[tuple(v for v in i if not isinstance(v,str)) for i in marks]
print(result)