POLYMORPHISM (Core Idea)
🔹 What is Polymorphism?

Polymorphism means “same method name, different behavior.”

One interface → many forms.

🔥 Why Polymorphism Exists (Real Reason)

Because in real systems:

You want to call one method

But behavior should change based on object

You don’t want if-else everywhere.

🧩 Example Before Polymorphism (BAD)
def make_payment(type, amount):
    if type == "upi":
        print("Paid via UPI")
    elif type == "card":
        print("Paid via Card")


Messy. Not scalable.

✅ With Polymorphism (GOOD)
payment.pay(amount)


Behavior depends on object type.

🔹 Types of Polymorphism in Python

We will focus on ONLY the important one:

✅ Method Overriding (MOST IMPORTANT)
🧱 Method Overriding (Core Concept)

Child class redefines a method of parent class.

Rule:

Same method name

Same parameters

Different implementation

🧪 Simple Example (WITHOUT abstraction)
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")


Usage:

a = Animal()
d = Dog()
c = Cat()

a.sound()
d.sound()
c.sound()

🔥 What happened?

Same method sound()

Different output

Python decides at runtime

This is runtime polymorphism.

🔹 Polymorphism + Abstraction (REAL USE)
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


Child classes:

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid {amount} via UPI")

class Card(Payment):
    def pay(self, amount):
        print(f"Paid {amount} via Card")


Generic function:

def process_payment(payment):
    payment.pay(500)


Usage:

process_payment(UPI())
process_payment(Card())

🧠 THIS is the MAGIC

Same method: pay()

Same function: process_payment()

Different behavior

No if-else

No code change when new payment added

📝 Ultra-Short Notes (Copy)
Polymorphism = Same method, different behavior
Achieved using method overriding
Decided at runtime
Works perfectly with abstraction