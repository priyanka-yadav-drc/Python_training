import math

x1=int(raw_input("x1: "))
x2=int(raw_input("x2: "))
y1=int(raw_input("y1: "))
y2=int(raw_input("y2: "))

x3=pow(abs(x2-x1),2)
y3=pow(abs(y2-y1),2)
dis=math.sqrt(x3+y3)

print(dis)