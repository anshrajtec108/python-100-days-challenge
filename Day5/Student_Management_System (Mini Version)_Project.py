'''PROJECT REQUIREMENTS (You Will Build This)
Class: Student

instance variables: name, roll, marks (dict)

instance method:

get_average()

print_details()

Class: StudentManager

class variable: total_students

instance variable: list of students

instance method:

add_student()

remove_student()

search_student()

show_all_students()

class method:

get_total_students()

static method:

validate_marks(marks) → marks should be 0–100'''

# Project
#  ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T
#  ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T
#  ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T ❌ T
#       Wrong code rewrite By me 
from functools import reduce

class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks  # marks is a dictionary: {"math": 90, "science": 85}

    # INSTANCE METHOD
    def get_average(self):
        # return average marks
        sumMarks=int(reduce(lambda a,b:  a+b, map(lambda x:x[1],self.marks.items())))
        avgMarks=sumMarks / int(len(self.marks))
        return avgMarks

    def print_details(self):
        # print roll, name, and all marks
       print(f"roll, {self.roll} name, {self.name} and all marks. {self.marks}")

class StudentManager:
    total_students = 0

    def __init__(self):
        self.students = []

    # INSTANCE METHOD
    def add_student(self, student):
         # add student to list
        # increase total_students using class variable
        self.students.append(student)
        StudentManager.total_students=int(len(self.students))
    def remove_student(self, roll):
        # remove student by roll number
        tempStudent=self.students
        findindex=0
        for i in range(len(tempStudent)):
            lenData=int(len(tempStudent[i]))
            BreakLoop=False
            for j in range(lenData):
                if(tempStudent[i][j]==roll):
                    findindex  = i
                    BreakLoop=True
                    break
                else:
                    continue
            if(BreakLoop):
                break
            else:
                continue
        
        self.students.pop(findindex)
        StudentManager.total_students=int(len(self.students))

    def search_student(self, roll):
        # find student and return it
        findedstudent=tuple(filter( lambda x:x[1] == roll,self.Student))
        return findedstudent

    def show_all_students(self):
        # print details of every student
        print(self.students)

    # CLASS METHOD
    @classmethod
    def get_total_students(cls):
        # return total number of students
        return cls.total_students

    # STATIC METHOD
    @staticmethod
    def validate_marks(marks):
        # check if all marks are 0–100
        if marks >= 0 and marks <= 100:
            print("The marks are validated (within the 0-100 range).")
        else:
            print("The marks are invalid (outside the 0-100 range).")

# # DRIVER CODE (MAIN PROGRAM)
# manager = StudentManager()

# # Example data (you can test with 3-4 students)
# s1 = Student("Ansh", 1, {"math": 95, "science": 90})
# s2 = Student("Raj", 2, {"math": 85, "science": 80})
# s3 = Student("Mohan", 3, {"math": 70, "science": 75})


# manager.add_student(s1)
# manager.add_student(s2)
# manager.add_student(s3)

# manager.show_all_students()
# print(StudentManager.get_total_students())

# s1.print_details()
# s2.print_details()
# s3.print_details()

# print(s1.get_average())
# print(s2.get_average())
# print(s3.get_average())

# StudentManager.validate_marks(50)
# StudentManager.validate_marks(-10)
# StudentManager.validate_marks(120)

# # ❌ TEST CASE 5 (Remove Student) — Your Function Will Currently FAIL
# manager.remove_student(2)
# manager.show_all_students()
# print("Total:", StudentManager.get_total_students())




from functools import reduce

# -----------------------------------------
# CLASS : Student
# -----------------------------------------
class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks   # dictionary: {"math": 90, "science": 80}

    # INSTANCE METHOD - average marks
    def get_average(self):
        total = sum(self.marks.values())
        return total / len(self.marks)

    # INSTANCE METHOD - print student details
    def print_details(self):
        print(f"Roll: {self.roll}")
        print(f"Name: {self.name}")
        print("Marks:")
        for subject, score in self.marks.items():
            print(f"  {subject}: {score}")
        print(f"Average: {self.get_average():.2f}")
        print("-" * 30)


# -----------------------------------------
# CLASS : StudentManager
# -----------------------------------------
class StudentManager:
    total_students = 0  # CLASS VARIABLE

    def __init__(self):
        self.students = []  # instance variable

    # INSTANCE METHOD - add student
    def add_student(self, student):
        self.students.append(student)
        StudentManager.total_students += 1

    # INSTANCE METHOD - remove student by roll
    def remove_student(self, roll):
        for s in self.students:
            if s.roll == roll:
                self.students.remove(s)
                StudentManager.total_students -= 1
                print(f"Student with roll {roll} removed.")
                return

        print("No student found with that roll number!")

    # INSTANCE METHOD - search student
    def search_student(self, roll):
        for s in self.students:
            if s.roll == roll:
                return s
        return None

    # INSTANCE METHOD - show all students
    def show_all_students(self):
        if not self.students:
            print("No students available.")
            return

        for s in self.students:
            s.print_details()

    # CLASS METHOD
    @classmethod
    def get_total_students(cls):
        return cls.total_students

    # STATIC METHOD
    @staticmethod
    def validate_marks(marks_dict):
        for m in marks_dict.values():
            if not (0 <= m <= 100):
                return False
        return True


# -----------------------------------------
# DRIVER CODE
# -----------------------------------------
manager = StudentManager()

# Example students
s1 = Student("Ansh", 1, {"math": 95, "science": 90})
s2 = Student("Raj", 2, {"math": 85, "science": 80})
s3 = Student("Rohit", 3, {"math": 78, "science": 88})

# Validate marks before adding
if StudentManager.validate_marks(s1.marks):
    manager.add_student(s1)

if StudentManager.validate_marks(s2.marks):
    manager.add_student(s2)

if StudentManager.validate_marks(s3.marks):
    manager.add_student(s3)

# Show all students
manager.show_all_students()

# Search
found = manager.search_student(2)
if found:
    print("FOUND STUDENT:")
    found.print_details()

# Remove
manager.remove_student(1)

# Display updated list
manager.show_all_students()

# Total students
print("Total Students:", StudentManager.get_total_students())
 
