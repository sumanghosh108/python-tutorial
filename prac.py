class Mobile:
    def os(self):
        print('Andriod')
class Realme():
    def spec(self):
        self.mobile=Mobile()
        self.mobile.os()
        print('8GB RAM, 256 GB storage')
obj=Realme()
# obj.spec()
# obj.os()
obj.spec()