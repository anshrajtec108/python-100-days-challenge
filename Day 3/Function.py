from functools import reduce


#Basic syntax
def greet():
    print("Hello!")
greet()

#Function with Parameters
def add(a,b):
    print(a+b)
add(2,5)
#Why important? : Inputs allow flexibility → same function works for many values.

#Default Parameters
def welcome(name="Ansh"):
    print("Welcome", name)

welcome() #Welcome Ansh
welcome("Raj") #Welcome Raj

#Keyword Arguments
def info(name, age):
    print(name, age)

info(age=20, name="Ansh")
#Order doesn’t matter

#Return Statement
# You can return:
   # Single value
   # Multiple values (as a tuple)
def calc(a, b):
    return a+b, a-b, a*b

x, y, z = calc(10, 5)
print(x, y, z)

#args → variable number of arguments
def total(*nums):
    print(nums[1])
    return sum(nums)

print(total(1,2,3))
print(total(10,20,30,40))
#👉 Receives values as tuple.

# kwargs → variable keyword arguments
def details(**data):
    print(data)

details(name="Ansh", age=20, city="Mysore")
#more example 
def student(**data):
    print("Name:", data["name"])
    print("Course:", data["course"])

student(name="Ansh", course="Python")
#👉 Receives values as dictionary.

#8️⃣ Lambda Function (Very Important for ML)
square = lambda x: x*x
print(square(5))
#more example 
add = lambda a,b : a+b
print(add(5, 7))
#more example
students = [("Ansh", 20), ("Raj", 18), ("Vishal", 25)]
students.sort(key=lambda x: x[1])   # sort by age
print(students)

#9️⃣ map() — Apply a function to every item
nums = [1,2,3,4]
result = list(map(lambda x: x*2, nums))
print(result)
#more example 
data = ["1", "2", "3"]
clean = list(map(int, data))
print(clean)

#🔟 filter() — Keep only items that satisfy a condition
nums = [1,2,3,4,5,6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
#example
names = ["Ansh", "Raj", "Michael", "David"]
long = list(filter(lambda x: len(x) > 4, names))
print(long)
 
#1️⃣1️⃣ reduce() — Combine values into a single result
nums = [1, 2, 3, 4]
result = reduce(lambda a, b: a + b, nums)
print(result)
result = reduce(lambda a, b: a*b, nums)
print(result)   # 24

#1️⃣2️⃣ Nested Functions
def outer():
    
    def inner():
        print("I am inner")
    print("outer1")
    inner()
    print("outer2")
outer()

#1️⃣3️⃣ Function Returning a Function
#👉 MOST IMPORTANT concept in Python.

def greet():
    def hello():
        return "Hello Ansh!"
    return hello

fn = greet()
print(fn())   # calling inner function
#Practical use-case
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15
