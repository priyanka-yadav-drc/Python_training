from collections import defaultdict

def test(*dicts):
  result = defaultdict(list)
  for el in dicts:
    for key in el:
      result[key].append(el[key])
  return dict(result)

d1 = {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
d2 = {'x': 300, 'y': 'Red', 'z': 600}

print(test(d1,d2))



