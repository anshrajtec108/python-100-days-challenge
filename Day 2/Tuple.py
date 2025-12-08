fruits = ("Apple", "Banana", "Orange", "Mango")
print(fruits)

print(fruits[0])
print(fruits[-1])

# fruits[0] = "Guava" TypeError: 'tuple' object does not support item assignment

print(fruits)

#📌 4. Tuple Unpacking
a, b, c = (1, 2, 3) 
print(a)

#📌 5. Convert between Tuple & List
print(type(fruits))
listOfTuple=list(fruits) # It will not change the Tuple data type it will be creating a temporary New list of the same elements
print(type(fruits)) #<class 'tuple'>
print(type(listOfTuple)) #<class 'list'>

nums = (1,2,3,4,2,2)

#Tuple METHODS
print("Tuple METHODS")
print(nums.count(2))
print(nums.index(4))
