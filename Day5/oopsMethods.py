# TYPES OF METHODS IN PYTHON
# There are 3 types of methods:

# ✔ 1. Instance Methods (most common)
class A:
    def show(self):
        print("Instance Method")
obj=A()
obj.show()

#✔ 2. Class Variable
#Because class methods are the ONLY methods allowed to change class variables.
class B:
    count = 5
    value = 0

    @classmethod
    def change_count(cls, val):
        cls.count = val

    def print(self):
        print("count =", B.count)

obj2 = B()
obj2.print()
obj2.change_count(9)
obj2.print()

#Static method = a normal function placed inside a class

class C:
    @staticmethod
    def add(a, b):
        return a + b
    
# ⭐ NOW — ONE CLASS USING ALL THREE METHODS
# 🔥 With comments explaining why each method is used

class Bank:
    # CLASS VARIABLE → shared by all customers
    bank_name = "SBI"

    def __init__(self, name, balance):
        # INSTANCE VARIABLES → different for each object
        self.name = name
        self.balance = balance

    # INSTANCE METHOD → needs object data (balance, name)
    def deposit(self, amount):
        if Bank.validate_amount(amount):
            self.balance += amount
            print(f"{self.name} deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    # CLASS METHOD → modifies class-level data (bank_name)
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name
        print(f"Bank name updated to: {cls.bank_name}")

    # STATIC METHOD → utility function (no self or cls required)
    @staticmethod
    def validate_amount(amount):
        return amount > 0


# ---- Testing ----
cust1 = Bank("Ansh", 5000)

cust1.deposit(1000)         # instance method usage
Bank.change_bank_name("HDFC")   # class method usage using updated bank name
cust1.deposit(500)         

# 1. Instance Method:
#    - Needs 'self'
#    - Uses object's data like balance
#    - deposit() is an instance method because balance is per customer

# 2. Class Method:
#    - Needs 'cls'
#    - Used to change class-level data (bank_name)
#    - change_bank_name() is a class method because bank_name is shared

# 3. Static Method:
#    - No self, no cls
#    - Just a helper logic
#    - validate_amount() is static because amount > 0 does not depend on object or class
