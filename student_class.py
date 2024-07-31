import os
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)


num = int(input('Enter number of students: '))  # Convert input to integer
os.system("cls")
students = []  # Create an empty list to store students

for i in range(num):
    name = input("Enter name: ")
    age = int(input("Enter age: "))  # Convert age to integer
    grade = input("Enter grade: ")
    student_i = Student(name, age, grade)
    os.system("cls")
    students.append(student_i)  # Append each student object to the list

# Display information of all students
count=0    

for student in students:
    count+=1
    print(f"\nStudent {count} : ")
    
    student.display_info()

os.system("pause>nul")
