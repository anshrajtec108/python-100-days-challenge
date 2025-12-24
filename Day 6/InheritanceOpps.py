# INHERITANCE — ONE PERFECT EXAMPLE (DEEP)
# 🔹 Real-world example: Employee System
# 🔸 Parent Class
class Employee:
    def __init__(self, name, salary):
        self.name = name        # common property
        self.salary = salary    # common property

    def show_details(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


# 👉 This class holds common data
# Every employee has a name and salary

# 🔸 Child Class
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)   # calls Employee constructor
        self.department = department

    def show_details(self):
        super().show_details()           # reuse parent method
        print("Department:", self.department)

   


# 🔸 Object Creation
m1 = Manager("Ansh", 50000, "IT")
m1.show_details()
e1=Employee("Kiran", 1000)
e1.show_details()

# Practice 1 — Real-world

class Account():
    def __init__(self,account_number,balance):
        self.__account_number=account_number
        self.__balance=balance
    
    def show_balance(self):
        print("balance",self.__balance)
    
    def get_balance(self):
        return self.__balance

class SavingsAccount(Account):
    def __init__(self, account_number, balance,interest_rate):
        self.interest_rate=interest_rate
        super().__init__(account_number, balance)
    
    def calculate_interest(self):
        interestAmout= ((super().get_balance()/100)*self.interest_rate)
        print("interestAmout = ",interestAmout)
        super().show_balance()

S1=SavingsAccount(1234567,5670,3.5)
S1.calculate_interest()