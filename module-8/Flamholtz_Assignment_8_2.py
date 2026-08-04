# Tzvi Flamholtz
# Assignment 8.2
# 08/02/2026
# This program reads a json file of students, adds a new student to the list, and writes the updated list back to the json file.

# Import json library
import json

# Define Student class of whats contained
class Student:
    def __init__(self, F_Name, L_Name, Student_ID, Email):
        self.F_Name = F_Name
        self.L_Name = L_Name
        self.Student_ID = Student_ID
        self.Email = Email

# Define StudentDecoder class to decode the json file into a Student object
class StudentDecoder(json.JSONDecoder):
    def __init__(self, object_hook=None, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, o):
        decoded_student =  Student(
            o.get("F_Name"), 
            o.get("L_Name"), 
            o.get("Student_ID"),
            o.get("Email"),
        )
        # Return the decoded student object
        return decoded_student

# Define a function to print the student list
def print_student(student_list):

    # Loop through the student list and print each student's information
    for s in student_list:
        print(f"{s.L_Name}, {s.F_Name} :ID = {s.Student_ID}, Email = {s.Email}")

# Read the Student.json file and decode it into a list of Student objects
with open('Student.json','r') as f:
    student_object = json.load(f, cls=StudentDecoder)

# Output message to the user and print the original student list
print("This is the original Student list.")
print_student(student_object)

# Add my info 
new_student = Student(
    "Tzvi",
    "Flamholtz",
    98765,
    "tflam@gmail.com"
    )

# Append the new student to the student list 
student_object.append(new_student)

# Output message to the user and print the updated student list
print("The Student list has been updated")
print_student(student_object)

# Define StudentEncoder class to encode the Student object into a json file
class StudentEncoder(json.JSONEncoder):
    def default(self, o): 
        if isinstance(o, Student):
            # Return a dictionary representation of the Student object
            return{
                    "F_Name": o.F_Name,
                "L_Name": o.L_Name,
                "Student_ID": o.Student_ID,
                "Email": o.Email
            }
        # If the object is not a Student object, call the default method of the parent class
        else:
            return super().default(o)

# Write the updated student list to the Student.json file
with open('Student.json','w') as json_file:
    json.dump(student_object, json_file, cls=StudentEncoder, indent=4)

# Output message to the user that the Student.json file has been updated
print("The Student .json file has been updated")

# Title: Flamholtz_Assignment_8_2.py
# Author: Tzvi Flamholtz some code taken from https://oxylabs.io/blog/python-parse-json
# date: 8/2/2026    
