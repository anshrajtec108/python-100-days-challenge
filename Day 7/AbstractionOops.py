from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        print("processing... ")
        pass

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid {amount} via UPI")

class Card(Payment):
    def pay(self, amount):
        print(f"Paid {amount} via Card")

u = UPI()
u.pay(500)

c = Card()
c.pay(1000)
