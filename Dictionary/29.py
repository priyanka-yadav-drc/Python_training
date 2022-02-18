student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
print("Original dictionary: ",student_list)
student_dict = {x.replace(" ",""): y for x, y in student_list.items()}
print("New dictionary: ",student_dict)
