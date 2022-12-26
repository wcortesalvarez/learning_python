student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for grade in student_scores:
  if student_scores[grade] <= 70:
    student_grades[grade] = "Fail"
  elif student_scores[grade] <= 80:
     student_grades[grade] = "Acceptable"   
  elif student_scores[grade] <= 90:
     student_grades[grade] = "Exceeds Expectations"
  else:
     student_grades[grade] = "Outstanding"    
  
print(student_grades)