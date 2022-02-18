def func(students,key,val):
	return any(s[key]==val for s in students)


students = [
        {'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, 
        {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
        {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, 
        {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, 
        {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}
        ]


print(func(students,'student_id',2))