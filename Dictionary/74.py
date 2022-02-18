def func(users,fn):
	return dict((k,fn(v)) for k,v in users.items())


users = {
  'Theodore': { 'user': 'Theodore', 'age': 45 },
  'Roxanne': { 'user': 'Roxanne', 'age': 15 },
  'Mathew': { 'user': 'Mathew', 'age': 21 },
}

print(func(users,lambda x: x['user']))