'''Practice 1 — Core (Must do)

Write a class with:
One private variable
One getter
One setter with validation

Example idea (don’t copy, write yourself):
Class: Student
Private: __marks
Condition: 0–100
If you can write this without help → concept is solid'''

class Student:
    def __init__(self,marks,name):
        self.__marks=marks #Private
        self.name=name 

    def get_marks(self):
        print(self.__marks)
    
    def set_marks(self, newMarks):
        if (newMarks>= 0 and newMarks<=100):
            self.__marks=newMarks
        else:
            print("Invalid marks ")

S1=Student(45,"Ansh Raj")
S1.get_marks()
S1.set_marks(100)
S1.get_marks()
print(S1.name)
# print (S1.__marks) #Error 