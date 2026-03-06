# Time Complexity in Python (DSA Notes)

## 1. What is Time Complexity?
Time Complexity is a way to measure **how the execution time of an algorithm grows** as the input size (`n`) increases.  
It helps us **compare algorithms** and choose the most efficient one.

We represent time complexity using **asymptotic notations**.

---

## 2. Types of Asymptotic Analysis

### 1️⃣ Best Case – Ω (Omega)
- Minimum time required
- Rarely used in practice

### 2️⃣ Average Case – Θ (Theta)
- Average running time
- Hard to calculate in real scenarios

### 3️⃣ Worst Case – O (Big O)
- Maximum time required
- **Most commonly used**
- Safe and reliable for analysis

👉 In real-world DSA, we mostly use **Big O notation**

---

## 3. Order of Growth (Comparison)

From fastest to slowest:

O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ)

yaml
Copy code

---

## 4. Constant Time – O(1)

### Definition:
Execution time does **not depend on input size**

### Example:
```python
x = 5
print(x)
Example with condition:
python
Copy code
if x == 5:
    print("Hello")
else:
    print("Welcome")
✔ Always takes constant time
✔ No loops involved

5. Linear Time – O(n)
Definition:
Execution time grows linearly with input size

Example:
python
Copy code
n = 5
for i in range(n):
    print(i)
Loop runs n times

Time complexity = O(n)

6. Quadratic Time – O(n²)
Definition:
Time grows proportional to square of input size
Common with nested loops

Example:
python
Copy code
n = 5
for i in range(n):
    for j in range(n):
        print(i, j)
Outer loop → n times

Inner loop → n times

Total operations = n × n = O(n²)

7. Cubic Time – O(n³)
Definition:
Three nested loops → cube growth

Example:
python
Copy code
n = 5
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i, j, k)
Total operations = n³

Time complexity = O(n³)

8. Logarithmic Time – O(log n)
Definition:
Input size is reduced by a constant factor each step
Very efficient

Example:
python
Copy code
n = 10
while n > 1:
    print("Hello")
    n = n // 2
Explanation:
swift
Copy code
n → n/2 → n/4 → n/8 → ... → 1
Number of steps = log₂ n

✔ Used in Binary Search

9. Mixed Time Complexity
Example:
python
Copy code
n = 5

print(n)                 # O(1)

for i in range(n):       # O(n)
    print(i)

for i in range(n):       # O(n²)
    for j in range(n):
        print(i, j)
Final Time Complexity:
mathematica
Copy code
O(1) + O(n) + O(n²) = O(n²)
👉 Always take the highest order term

10. Important Rules
Ignore constants

scss
Copy code
O(2n) → O(n)
Ignore lower-order terms

scss
Copy code
O(n² + n) → O(n²)
Nested loops multiply

scss
Copy code
O(n) × O(n) → O(n²)
11. Mathematical Examples
Function Type	Equation	Time Complexity
Constant	y = 5	O(1)
Linear	y = 2n + 5	O(n)
Quadratic	y = n² + 3n	O(n²)
Cubic	y = n³ + 2n²	O(n³)
Logarithmic	y = log n + 2	O(log n)

12. Key Revision Notes
No loop → O(1)

One loop → O(n)

Nested loops → O(n²), O(n³)

Divide input → O(log n)

Always consider worst case

