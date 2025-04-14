# Creating a dictionary with student names and their marks
student_marks = {
    "Ram": 85,
    "Sham": 92,
    "Stive": 78,
    "Farhan": 88,
    "mike": 95
}

# Asking the user to input a student's name
student_name = input("Please enter the student's name: ")

if student_name in student_marks:
    print(f"{student_name}'s marks are: {student_marks[student_name]}")
else:
    print(f"{student_name} not found.")

