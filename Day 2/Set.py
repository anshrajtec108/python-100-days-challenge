# ✅ 1. SET in Python
# A set is:
# Unordered
# Unique elements only
# Fast for search (O(1))
# Mutable (you can add/remove)

s = {1,2,3}
s.add(4)
print(s)

s.remove(2)   # gives error if 2 not found
s.discard(5)  # safe, no error if 5 not found
print(s)

value = s.pop()
print(value)
print(s)

s.clear()
print(s) #clear all the elements

# 📌📌📌 Set Operations (VERY important for interviews + ML)
a = {1,2,3}
b = {3,4,5}
print(a,b)
#Union
print(a | b)     # OR  Meaning: All unique elements from both sets. : {1, 2, 3, 4, 5}
#Intersection
print(a & b) #Common elements both set :  {3}
#Difference
print(a - b) # Unique Only in A, not in B : {1, 2}
#Symmetric Difference
print(a ^ b) # Items that are NOT common — unique to each set. : {1, 2, 4, 5}

print(a.isdisjoint(b))  # no common elements True/False
print(a.issubset(b)) # a inside other?
print(a.issuperset(b)) #a contains other?

 
#MICRO PRACTICE
print("MICRO PRACTICE")
prSet= {10, 20, 30}
prSet.add(40)
prSet.discard(20)
print(prSet)
print(prSet | {30, 50, 60})