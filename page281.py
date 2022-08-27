from abc import ABC, abstarctmethode

class Mall(ABC):
    def coupon(self, amount):
        print("Your coupon amount: ",amount)

    @abstractmethod
    def discount(self, amount):
        pass

class CreditPayment(Mall):
    def discount(self, amount):
        print("your credit limit has been exeed you $1000 ".format(amount))

obj = CreditPayment()
obj.coupon("$1100")
obj.discount("$5200")


     
    
