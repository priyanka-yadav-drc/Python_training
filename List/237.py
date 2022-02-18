simpsons = [
  { 'name': 'Areeba', 'age': 8 },
  { 'name': 'Zachariah', 'age': 36 },
  { 'name': 'Caspar', 'age': 34 },
  { 'name': 'Presley', 'age': 10 }
]
key='name'
result=[x.get(key) for x in simpsons]
print(result)