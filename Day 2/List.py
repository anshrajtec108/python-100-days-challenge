# print(type(10))
# print(type(10.5))
# print(type("Ansh"))
# print(type(True))
# print(type([1,2,3]))
# print(type((1,2,3)))
# print(type({1,2,3}))
# print(type({"name":"Ansh"}))

numbers = [ 1, 2, 3, 4, 5 ]
print(numbers)

numbers.append(6)
print(numbers)

numbers.remove(5)
print(numbers)
#Sum
print(sum(numbers))
#Indexing
print(numbers[3])
print(numbers[-1])
#Update value
numbers[-1]=100
print(numbers)

#Nested List
matrix = [[1,2,3],[4,5,6]]
print(matrix[0][1]) #2
print(matrix[1][1]) #5

#List Slicing
print(numbers[1:4])   # from index 1 to 3

#📌 3. List Comprehension (Very Important for ML)
squares = [x*x for x in range(1,6)]
print("squares =", squares)

#📌 5. Convert between List & Tuple
tupleData  =tuple(numbers)
print(type(tupleData))

 
#LIST METHODS
print("LIST METHODS")
print(len(numbers))   # total elements

numbers.insert(1, 999)   # insert at index 1
print(numbers)

numbers.extend([200, 300])
print(numbers)

last = numbers.pop()
print(last)
print(numbers)

numbers.pop(2)   # remove value at index 2
print(numbers)

#sort() and reverse()
print("sort and reverse")
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

#count() and index()
print(numbers.count(3))   # how many 3s
print(numbers.index(4))   # index of 4

#MICRO PRACTICE
print("MICRO PRACTICE")
list= [10,20,30,40,50]
list.insert(2,25)
print(list)
#Delete the last element
list.pop()
#Sort it in descending order
list.sort(reverse=True)
print("descending order list", list)
#Convert it into tuple
theTuple=tuple(list)
print(type(theTuple))