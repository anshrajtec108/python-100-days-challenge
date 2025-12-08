#List
#1. Create a list of numbers 1–10. and Print even numbers using slicing.
List = [1,2,3,4,5,6,7,8,9,10]
print(List[1::2])
#2Insert 100 at index 3, remove number 5
List[3]=100
List.remove(5)
print(List)
#3. Sort the list in descending order.
List.sort(reverse=True)
print(List)
#4. Create a nested list: Print 4 → Replace 6 with 99
matrix = [[1,2],[3,4],[5,6]]
print(matrix[1][1])
matrix[2][1]=99
print(matrix)
#5. Generate list of cubes from 1–10 using list comprehension
cubes=[x*x*x for x in range(1,10) ]
print(cubes)


#🟧 TUPLE Questions
print(" TUPLE Questions")
#6. Create a tuple of 5 names. and Print first and last name
names_tuple = ("Alice", "Bob", "Charlie", "David", "Eve")
print(names_tuple[0])
print(names_tuple[-1])
#Convert the tuple to list, add one more name, convert back to tuple.
tempList=list(names_tuple)
tempList.append("Ansh")
names_tuple=tuple(tempList)
print(names_tuple) 
print(type(names_tuple))

#🟩 SET Questions
print("SET Questions")
#9 Create two sets: and find Union, Intersection , Difference and Symmetric difference
a = {1,2,3,4}
b = {3,4,5,6}
#Union
print(a|b)
# Intersection
print(a&b)
# Difference
print(a-b)
# Symmetric difference
print(a^b)

# 10. Remove duplicates from this list using set:
lst = [1,1,2,3,3,3,4,5,5]
setList=set(lst)
print(setList)
#11 Check
{1,2}.issubset({1,2,3})
{1,2,3}.issuperset({1,2})

#🟨 DICTIONARY Questions
# 12. Create dictionary:
# Perform:
# Update score to 95
# Add city = “Mysuru”
# Remove course
# Print all keys
# Print all values
student = {
  "name": "Ansh",
  "course": "Python",
  "score": 85
}
student.update({"score":95})
student["city"]="Mysore"
student.pop("course")
print(student)
print(student.keys())
print(student.values())
print(student.items())

