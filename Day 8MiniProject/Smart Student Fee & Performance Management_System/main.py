# Main program & menu logic
from functools import reduce


student_list=[]
# Base User Class (Inheritance starts here)
class User():
    def __init__(self, user_id, name):
        self.user_id=user_id
        self.name=name

class Admin(User):
        def __init__(self, user_id, name):
            super().__init__(user_id, name)

        def add_student(self, student_list):
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
        
            for student in student_list:
                if student.user_id == student_id:
                    print("Student ID already exists!")
                    return

           # Create Student object
            new_student = Student(student_id, name)

            # Add to list
            student_list.append(new_student)

            print("Student added successfully!")

        def view_all_students(self, student_list):
            print("\nStudents in system:")
            for s in student_list:
                print(s.user_id, s.name)



class Student(User):
    def __init__(self, student_id, name):
        super().__init__(student_id, name)
        self.__marks = []          # private
        self.__fee_paid = False    # private

    def add_marks(self, marks):
        self.__marks.append(marks)
        print("The marks is successfully added!")

    def calculate_average(self):
        print("calculate_average -- ",sum(self.__marks) / len(self.__marks))

    def pay_fee(self, payment_method):
        pass


#CALL 
admin = Admin("A001", "Admin")

admin.add_student(student_list)
admin.add_student(student_list)
admin.view_all_students(student_list)

