x=int(raw_input("Num1: "))
y=int(raw_input("Num2: "))
if x > y:
      z = x
else:
      z = y
while(True):
      if((z % x == 0) and (z % y == 0)):
          lcm = z
          break
      z += 1
  
print(lcm)