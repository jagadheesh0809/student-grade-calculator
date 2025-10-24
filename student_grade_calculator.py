# student_grade_calculator.py

results = []

def calculate_grade(marks):
    if marks >= 90:
        grade = 'A+'
        comment = 'Excellent performance!'
    elif marks >= 80:
        grade = 'A'
        comment = 'Very good job!'
    elif marks >= 70:
        grade = 'B'
        comment = 'Good effort, keep improving.'
    elif marks >= 60:
        grade = 'C'
        comment = 'Satisfactory, needs some improvement.'
    elif marks >= 50:
        grade = 'D'
        comment = 'Below average, work harder.'
    else:
        grade = 'F'
        comment = 'Failed. Better luck next time.'
    return grade, comment

def add_student_result(name, marks):
    grade, comment = calculate_grade(marks)
    result = {
        'Name': name,
        'Marks': marks,
        'Grade': grade,
        'Comment': comment
    }
    results.append(result)
    return result

# Example usage:
add_student_result('Alice', 92)
add_student_result('Bob', 76)
add_student_result('Charlie', 58)

print(results)
