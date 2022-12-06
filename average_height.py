student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

longitud = len(student_heights)
suma = sum(student_heights)

average = round(suma / longitud)
print(average)