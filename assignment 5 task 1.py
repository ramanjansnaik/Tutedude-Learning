'''
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
'''


students = { 'dan':95 , 'tom':96 , 'sam':98 , 'pam':92 }

name = input("Please enter the student name from the list\n dan\n tom\n sam\n pam\n : ")

if name in students:
    print(f" The student has obtained {students[name]} Marks")
else:
    print("Student name not found")