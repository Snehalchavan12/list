# list
1]Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.

     student_marks = {
    "Ram": 85,
    "Sham": 92,
    "Stive": 78,
    "Farhan": 88,
    "mike": 95
     }

    student_name = input("Please enter the student's name: ")

    if student_name in student_marks:
    print(f"{student_name}'s marks are: {student_marks[student_name]}")
    else:
    print(f"{student_name} not found.")

2]Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list

    numbers = [ 1, 2, 3, 4,  5, 6, 7, 8, 9, 10 ]
    print ("Original list",numbers)
    print ("Extract first five element",numbers[0:5])

    a = [1, 2, 3, 4, 5]
    a.reverse()
    print("reverse extract element ",a)

    
   
