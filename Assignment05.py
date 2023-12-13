# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   JHuang, 12/13/2023, Completed Script
# ------------------------------------------------------------------------------------------ #
# Import json Module
import json
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"
#for testing, use raise Exception()
# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict[str,str] = {}  # Type dictionary
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.

#Load existing file contents, if applicable.
try:
   file = open(FILE_NAME, "r")
   raise Exception()
   students=json.load(file)
   file.close()
#Present an error if 'Enrollments.json' does not exist
except FileNotFoundError:
    print('File not found. Creating file.')
    open(FILE_NAME, 'w')
except Exception as e:
    print('Unknown exception. Resetting.')
    students = []
    print(type(e), e, sep='\n')
finally:
    file = open(FILE_NAME, "r")
    if file and not file.closed:
        file.close()

# Present and Process the data
while (True):
    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")
    # Input user data
    if menu_choice == "1":
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError ('Error: First name must be alphabetic')
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError('Error: Last name must be alphabetic')
            course_name = input("Please enter the name of the course: ")
            if not course_name:
                raise ValueError('Error: Course name cannot be blank')
            student_data = {'first_name':student_first_name,'last_name':student_last_name,'course_name':course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print(e)
        continue
    # Present the current data
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        for student in students:
            print(f'{student["first_name"]} {student["last_name"]} is enrolled in {student["course_name"]}.')
        continue
    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students,file)
            file.close()
            print("The following data was saved to file!")
            for student in students:
                print(f"Student {student['first_name']} {student['last_name']} is enrolled in {student['course_name']}.")

        except Exception as e:
            print('Error saving data to file.')
            print(e)
        finally:
            if file and not file.closed:
                file.close()
    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")
print("Program Ended")