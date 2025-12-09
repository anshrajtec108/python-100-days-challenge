from functools import reduce


#✅ MAP Questions
#1. Convert list of strings → integers
a=["1","2","3","4"]
print(list(map(int,a)))

#2. Square every number
b=[2, 4, 6]
print(list(map(lambda x:x*x,b)))

#3.Convert temperature C → F
#Formula: F = C * 1.8 + 32
c=[0, 10, 25]
print(list(map(lambda x:x*1.8+32,c)))

#4.Names → Uppercase
d=["ansh", "raj", "vishal"]
print(list(map(lambda x:x.upper(),d)))

#5.Increase age by 1
e=[("Ansh", 20), ("Raj", 18)]
print(list(map(lambda x: x[1]+1,e)))

#✅ FILTER Questions
print("FILTER Questions")
#6. Even numbers
f=[1,2,3,4,5,6]
print(list(filter(lambda  x: x%2==0,f)))

#7. Names longer than 4 letters
g=["Ansh", "Raj", "Vishal", "Rohan"]
print(list(filter(lambda x: len(x)>4,g)))

#8. Numbers divisible by 3
h=[3, 4, 6, 7, 9, 10]
print(list(filter(lambda x: x%3==0,h)))

#9. Words starting with "A"
i=["Apple", "Banana", "Avocado", "Orange"]
print(list(filter(lambda x:x[0]=="A",i)))

#10. Students age > 18
j=[("Ansh",20), ("Raj",17), ("Vishal",22)]
print(list(filter(lambda x:x[1]>18,j)))

#REDUCE Questions
print("REDUCE Questions")
#11. Sum of numbers
k=[1, 2, 3, 4]
print(reduce(lambda a,b : a+b,k))

#12. Product of numbers
print(reduce(lambda a,b : a*b,k))

#13.Maximum using reduce
l=[5, 1, 9, 3]
print(reduce(lambda a,b: max(a,b),l))

#14.Minimum using reduce
print(reduce(lambda a,b: min(a,b),l))

#15. Join strings
m=["Hello", "Ansh", "Raj"]
print(reduce(lambda a,b:a+b,m))

#MIXED TASKS
