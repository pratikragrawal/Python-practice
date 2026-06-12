def calculate_percentage(marks):
    total_marks = sum(marks)
    return (total_marks / (5 * 100)) * 100

def calculate_cgpa(percentage):
    return percentage / 10

def determine_grade(cgpa):
    if 0 <= cgpa <= 3.4:
        return 'F'
    elif 3.5 <= cgpa <= 5.0:
        return 'C+'
    elif 5.1 <= cgpa <= 6.0:
        return 'B'
    elif 6.1 <= cgpa <= 7.0:
        return 'B+'
    elif 7.1 <= cgpa <= 8.0:
        return 'A'
    elif 8.1 <= cgpa <= 9.0:
        return 'A+'
    elif 9.1 <= cgpa <= 10.0:
        return 'O'
    else:
        return 'Invalid CGPA'
subject_marks = [float(input(f"Enter marks for Subject {i + 1}: ")) for i in range(5)]



percentage = calculate_percentage(subject_marks)
cgpa = calculate_cgpa(percentage)
grade = determine_grade(cgpa)

print(" Name: Pranjal Goyal")
print(" Roll number: R2142231659")
print(" Sem: 1")
print("  subject name:  Marks")
print(" Mathematics:    90")
print(" Problem solving:    90")
print(" Linux:    90")
print(" C programming:    90")
print(" Enviornment:    90")
print(f"\n  Percentage: {percentage:.2f}%")
print(f"   CGPA: {cgpa:.2f}")
print(f" Grade: {grade}")

