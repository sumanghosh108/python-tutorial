# 18/09/25
# ----------------------------------------------------------------------------

'''
Access specifiers
public, private, protected
    - public :
        name='abc'
            - public variable and method can access anywhere in the program (inside and outside the class)
            - updation is possible inside and outside the class
    - protected :
        _var
        _method()
            - 
    - private :
        __variablename
        __methodname()
    
'''

'''
=>> Note:

'''

'''class Instagram:
    def __init__(self):
        self.u_name=input('Enter your name: ')
        self.u_id=input('Enter youe user ID: ')
        self._u_mno=input('Enter your M no : ') # protected variable
        self.following=0
        self.followers=0
    def display(self):
        print(f'Name : {self.u_name}\nFollowers : {self.followers}\nFollowing : {self.following}')
        print(f'Mobile number : {self._u_mno}') # Accessing public variable ✅
    def check(self):
        # self.u_name='abc' # public variable updation ✅
        # self.display() # Accessing public method ✅
        self._check1() # # Accessing protected method ✅
    def _check1(self):
        print('Accessing protected method....')
user1=Instagram()
# user1._check2()
# print(user1._u_mno) # Accessing protected variable ✅ but not recommendable ❌
# user1.dispaly()
# user1.check()
# user1.u_name='qwe' # public variable updation ✅
# user1.display() # Accessing public method ✅
# user1._check1() # Accessing protected method ✅ but not recommendable ❌
user1.check()'''

# ----------------------

'''class Snapchat:
    name='Snapchat'
    def __init__(self):
        self.__streaks=150
    def __display(self):
        print(self.__streaks)
    def disp(self):
        # print(self.__streaks) # private variable is possible to access inside the class ✅✅✅
        # self.__display() # private method is possible to access inside the class ✅✅✅
        # self.__streaks=200 # private variable is possible to update inside the class
        self.__display()
user1=Snapchat()
# user1.__display() # private method is not possible to access outside the class ❌❌❌
# print(user1.__streaks) # private variable is not possible to access outside the class ❌❌❌
user1.__streaks=300
print(user1.__streaks)
user1.disp()'''

# -------------------------------------------

'''
    how to access private method and variable outside the class ?
    --> by using getter() and setter() method
'''
'''class LinkedIn:
    def __init__(self):
        self.__connections =2000
    def getter(self):
            print(self.__connections)
    def setter(self,c):
            self.__connections = c
user1=LinkedIn()
user1.getter()
user1.setter(2500)
user1.getter()'''

# ------------------

class Flipkart:
    name='Flipkart'
    def __init__(self):
        self.__m_no=9800202833
        self.u_name='suman'
        self._wishlist=25
        self._cart=4
    def display(self):
        print(self.u_name)
        print(self.__m_no)
        print(self._cart)
    def __disp(self):
        self._cart=5
        print(self._cart)
        
    
user1=Flipkart()
user1.display()
user1.__disp()
# user1.+
# __disp()  # AttributeError: 'Flipkart' object has no attribute '__disp'
# print(user1._wishlist) # 25
# print(user1.u_name) # suman
# print(user1.__cart) # AttributeError: 'Flipkart' object has no attribute '__cart'