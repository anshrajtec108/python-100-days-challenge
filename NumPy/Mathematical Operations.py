import numpy as np

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a + b)
print(a - b)
print(a * b)
print(a / b)

print([1,2,3] + [4,5,6] ) # ❌ gives [1,2,3,4,5,6]

#2. SCALAR OPERATIONS
print("2. SCALAR OPERATIONS")

a = np.array([10,20,30])

print(a + 5)
print(a * 2)

#3. BUILT-IN FUNCTIONS
print("3. BUILT-IN FUNCTIONS")

a = np.array([10,20,30])

print(np.add(a, 5))
print(np.subtract(a, 5))
print(np.multiply(a, 2))
print(np.divide(a, 2))

#POWER OPERATIONS
print("POWER OPERATIONS")
print(a ** 2)

#2D ARRAY OPERATIONS
print("2D ARRAY OPERATIONS")
A = np.array([
    [1,2],
    [3,4]
])

B = np.array([
    [5,6],  
    [7,8]
])

print(A + B)

#MINI PROJECT 4: SALARY INCREMENT SYSTEM
print("MINI PROJECT 4: SALARY INCREMENT SYSTEM")


salary = np.array([20000, 25000, 30000, 35000])

#Add 10% bonus
bonus_salary = salary + (salary * 0.10)
print("Add 10% bonus",bonus_salary)
#Deduct tax (5%)
final_salary = bonus_salary - (bonus_salary * 0.05)
print("Deduct tax - 5%",final_salary)

'''🔥 BONUS (IMPORTANT FOR ML)

Matrix multiplication:'''
print("Matrix multiplication")

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

print(A @ B)
print(A * B)
