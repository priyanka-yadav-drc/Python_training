students = {
  'Theodore': 19,
  'Roxanne': 22,
  'Mathew': 21,
  'Betty': 20
}
max_d=max(students, key=students.get)
min_d=min(students,key=students.get)

print(students)
print("max: {}".format(max_d))
print("min: {}".format(min_d))