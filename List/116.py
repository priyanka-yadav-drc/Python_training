from operator import itemgetter
students = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] 

n=1
result=sorted(students,key=itemgetter(n))
print(result)