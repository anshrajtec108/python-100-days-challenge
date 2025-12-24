🧠 OOPS — THE 4 PILLARS (MASTER NOTES)
1️⃣ ENCAPSULATION
🔹 Definition

Encapsulation means binding data and methods together and protecting data from outside access.

In simple words:

Data protection + controlled access

🔹 Why Encapsulation Exists

Prevents direct access to data

Avoids accidental modification

Improves security

Makes code safer

🔹 How it is Achieved

Using private / protected variables

Using getter and setter methods

🔹 Example (Idea level)
class BankAccount:
    def __init__(self):
        self.__balance = 0   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

🔹 When to Use Encapsulation

✔ When data must be protected
✔ When rules must be enforced
✔ When security matters

🔹 One-Line Note
Encapsulation = Protect data, allow controlled access

2️⃣ ABSTRACTION
🔹 Definition

Abstraction means hiding implementation details and showing only essential features.

In simple words:

WHAT to do, not HOW to do

🔹 Why Abstraction Exists

Forces structure

Reduces complexity

Controls system design

Prevents developer mistakes

🔹 How it is Achieved

Abstract classes

Abstract methods (abc module)

🔹 Example (Idea level)
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

🔹 When to Use Abstraction

✔ When same action has different implementations
✔ When designing large systems
✔ When you want to enforce rules

🔹 One-Line Note
Abstraction = Hide how it works, show what must be done

3️⃣ INHERITANCE
🔹 Definition

Inheritance allows a class to acquire properties and methods of another class.

In simple words:

Reuse existing code

🔹 Why Inheritance Exists

Avoid code duplication

Improve reusability

Create parent-child relationship

🔹 How it is Achieved

Child class inherits parent class

🔹 Example (Idea level)
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

🔹 When to Use Inheritance

✔ When classes share common behavior
✔ When relationship is IS-A
✔ For code reuse

🔹 One-Line Note
Inheritance = Reuse code by creating parent-child relationship

4️⃣ POLYMORPHISM
🔹 Definition

Polymorphism means same method name but different behavior.

In simple words:

One interface, many forms

🔹 Why Polymorphism Exists

Avoid if-else chains

Write flexible code

Support future extensions

🔹 How it is Achieved

Method overriding

Runtime decision

🔹 Example (Idea level)
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

🔹 When to Use Polymorphism

✔ When same action behaves differently
✔ When using abstraction
✔ When system must scale

🔹 One-Line Note
Polymorphism = Same method, different behavior

| 🧱 Pillar            | 🎯 Main Focus | ❓ Question It Answers     | 🛠️ What It Actually Does                                  | 🧠 Easy Memory Symbol |
| -------------------- | ------------- | ------------------------- | ---------------------------------------------------------- | --------------------- |
| 🔒 **Encapsulation** | Data Safety   | **How to protect data?**  | Hides data & allows controlled access using methods        | 🔐 Lock               |
| 🎭 **Abstraction**   | Design Rules  | **What should be done?**  | Defines mandatory methods without logic (blueprint)        | 📜 Contract           |
| 🧬 **Inheritance**   | Code Reuse    | **What can be reused?**   | Child class reuses parent class properties & methods       | 🌳 Tree               |
| 🔁 **Polymorphism**  | Flexibility   | **How behavior changes?** | Same method name behaves differently for different objects | 🎨 Colors             |

🧠 GOLDEN MEMORY TRICK

Encapsulation → Protect

Abstraction → Design

Inheritance → Reuse

Polymorphism → Flexibility