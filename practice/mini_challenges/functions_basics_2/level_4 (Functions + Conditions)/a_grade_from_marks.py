# Write a function that calculated a grade from marks.

def calculate_grade(marks):
    grade = ''
    if marks >= 90 and marks <= 100:
        grade = 'A+'
    elif marks >= 80 and marks < 90:
        grade = 'A'
    elif marks >= 70 and marks < 80:
        grade = 'B'
    elif marks >= 60 and marks < 70:
        grade = 'C'
    elif marks >= 50 and marks < 60:
        grade = 'D'
    elif marks >= 33 and marks < 50:
        grade = 'E'
    elif marks >= 0 and marks <= 32:
        grade = 'F'
    else:
        return 'Invalid Marks!'

    return grade

result = calculate_grade(55)

print(result)