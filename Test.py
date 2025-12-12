# from functools import reduce

# marks={"math": 95, "science": 90}
# sumMarks=int(reduce(lambda a,b:  a+b, map(lambda x:x[1],marks.items())))
# avgMarks=sumMarks / int(len(marks))
# print( avgMarks)

student =[]
student.append(("Ansh", 1, {"math": 95, "science": 90}))
student.append(("Raj", 2, {"math": 85, "science": 80}))
print(student)

# tempStudent=student
roll=2
# findindex=0
# for i in range(len(tempStudent)):
#     print(len(tempStudent[i]))
#     lenData=int(len(tempStudent[i]))
#     BreakLoop=False
#     for j in range(lenData):
#         if(tempStudent[i][j]==roll):
#             findindex  = i
#             BreakLoop=True
#             break
#         else:
#             continue
#     if(BreakLoop):
#         break
#     else:
#         continue

# student.pop(findindex)
# print(student)

findedstudent=tuple(filter( lambda x:x[1] == roll,student))
print(findedstudent)