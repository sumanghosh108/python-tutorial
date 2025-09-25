from abc import ABC,abstractmethod
#Abstraction class
class ATM(ABC):
    # abstaract method
    @abstractmethod
    def withdraw(self):
        pass
print('file 3...')