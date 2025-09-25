# 24/09/25
# -----------------------------------------------------------------------------------------


'''
Abstraction :
    hides implementation & provides the functionality to the user
    Ex: Car,ATM,UPI
    
    step 1:
        from abc import ABC, abstractmethod
    step 2:
        Creation of Abstraction class
    step 3:
        Inherit AbC class
    step 4:
        hide the implementation of abstractmethod(pay) by using
'''

'''from abc import ABC,abstractmethod
#Abstraction class
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
#Concrete class
class UPI(Payment):
    def pay(self):
        print('Welcome to UPI payment .......')
class NetBanking(Payment):
    def pay(self):
        print('Welcome to NetBanking .......')

upi=UPI()
# pay_=Payment() # TypeError
# pay_.pay()
upi.pay()
'''
'''
from abc import ABC,abstractmethod
#Abstraction class
class Payment(ABC):
    # abstaract method
    @abstractmethod
    def pay2(self):
        pass
    # normal instance method
    def website(self):
        print('Opening website ...')
#Concrete class
class UPI(Payment):
    # concrete method
    def pay1(self):
        print('Welcome to UPI payment .......')
    # concrete method
    def pay2(self):
        print('Option 2 .......')
class NetBanking(Payment):
    def pay1(self):
        print('Welcome to NetBanking .......')

upi=UPI()
# pay_=Payment() # TypeError
# pay_.pay()
# upi.pay2()
# upi.pay1()
upi.website()
'''


from abc import ABC,abstractmethod
#Abstraction class
class Payment(ABC):
    # abstaract method
    @abstractmethod
    def pay2(self):
        pass
    # normal instance method
    def website(self):
        print('Opening website ...')
#Concrete class
class UPI(Payment):
    # concrete method
    def pay1(self):
        print('Welcome to UPI payment .......')
    # concrete method
    def pay2(self):
        print('Option 2 .......')
        super().pay2() # ❌❌❌❌
class NetBanking(Payment):
    def pay1(self):
        print('Welcome to NetBanking .......')

upi=UPI()
# pay_=Payment() # TypeError
# pay_.pay()
upi.pay2()
# upi.pay1()
# upi.website()

