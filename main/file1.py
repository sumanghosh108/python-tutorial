from abc import ABC,abstractmethod
#Abstraction class
class Payment(ABC):
    # abstaract method
    @abstractmethod
    def pay2(self):
        pass
def fun():
    print('file 11 fun')
fun()
print('file 1...')