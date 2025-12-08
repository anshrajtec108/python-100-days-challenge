student = {
    "name": "Ansh",
    "age": 20,
    "skills": ["Python", "SQL"],
}

# Access values
print(student["name"])
print(student.get("age"))
print(student.get("skills")[1])

# Add / Update values
student["city"] = "Mysuru"
student["age"] = 21

#Delete keys
student.pop("age")
del student["skills"]
print(student) #{'name': 'Ansh', 'city': 'Mysuru'}

#Loop through dictionary
for key, value in student.items():
    print(key, value)

#Useful dictionary methods
print(student.keys())
print(student.values())
print(student.items())
student.popitem()    # removes last inserted pair
student.setdefault("x", 0)  # adds only if missing
print(student)
student.clear()      # empty dict

#MICRO PRACTICE
print("MICRO PRACTICE")
emp = {
    "name": "Ansh",
    "age": 20,
    "role": "Data Science Student"
}
emp["city"]="Mysore"
emp["age"]="21" 

print(emp)
emp.update({"age": 25})

for key, value in emp.items():
      print(key, value)