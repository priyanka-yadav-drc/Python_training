students = [
  { 'name': 'Theodore', 'age': 18 },
  { 'name': 'Mathew', 'age': 22 },
  { 'name': 'Roxanne', 'age': 20 },
  { 'name': 'David', 'age': 18 }
]

result=[x.get('name') for x in students]
print(result)