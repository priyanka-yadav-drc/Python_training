from operator import itemgetter
class_students = [('VI', 60), ('V', 70), ('VII', 75), ('VIII', 72), ('IX', 78), ('X', 70)]
return_max = max(class_students,key=itemgetter(1))[1]
return_min = min(class_students,key=itemgetter(1))[1] 
print(return_min)

print(return_max)