name= input("Enter your name")
print ("your name is ", name , "And Your name type", type(name))

#TASK 1 — Addition using input
a=int(input("Number1  "))
b=int(input("Number2 "))
print("Result", a+b)

#TASK 2 — Name + Future Age
Name=input("Enter your name ")
Age=input("Enter your Age ")
print("Hello ",Name,". You will be ",Age," next year.") 

#TASK 3 — Small formatting challenge
startRange= int(input("starting range number "))
endRange= int(input("End  range number "))
for i in range(startRange, endRange + 1):
        print(f"{i:<3} {i*i}")

