#OOP BASICS PRACTICE (3 QUESTIONS)

#Create a class Car with attributes brand and price. And Create two objects and print their values.**
class car:
    def __init__(self,carname,price):
        self.carname=carname
        self.price=price
c1=car("BMW",987654)
c2=car("Toyota",456778)
print(c1.carname,c1.price)
print(c2.carname,c2.price)

# Create a class Student with a constructor that accepts name and marks. -- Print: "Ansh scored 95"**
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print(f"{name} scored {marks}")

s1=Student("Ansh",95)

# **3️⃣ Create a class Dog with a class attribute species = "Mammal".
# Every dog object should have name & age.
# Create 2 dogs and print:**
# name
# age
# species

class Dog:
    species = "Mammal"
    name_Var=" "
    def __init__(self,name,age):
        Dog.name_var=name # storing in class variable
        self.name=name
        self.age=age
    def printFun(self):
        print("name : ",self.name, "Dog.name_var= ",Dog.name_var, "age: ", self.age, "species : ",self.species)
D1=Dog("GPT",13)
d2 = Dog("Tommy", 5)

D1.printFun()
d2.printFun()


