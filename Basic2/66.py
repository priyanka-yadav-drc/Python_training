def func(n):
  past = set()
  while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in past:
            return "Not happy number"
        past.add(n)
  return "happy number"
print(func(7))
print(func(932))
print(func(6))
