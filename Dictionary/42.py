marks = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
print(marks)

marks={x:y for (x,y) in marks.items() if y>=180}

print("marks>=180 :")
print(marks)