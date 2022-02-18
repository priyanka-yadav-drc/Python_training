students = {
  'Theodore': 10,
  'Mathew': 11,
  'Roxanne': 9,
}

result=dict()

result={x:y for y,x in students.items()}
print(result)