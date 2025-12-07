'''
Data Type
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''
#Task 1 — Variables + type + conversion
a=5
b=2.5
c="7"
print(type(a))
print(type(b))
print(type(c))
print(a + int(c) + b)
#print(a + c + b) #TypeError

#Task 2 — Conversion test Convert it to int and Divide by 4
x = "100"
print(int(x)/4)

#Task 3 — Truthiness test
E=0
F=""
G=[]
H=None
I=1
print(bool(E)) #False
print(bool(F)) #False
print(bool(G))#False
print(bool(H))#False
print(bool(I))#True     