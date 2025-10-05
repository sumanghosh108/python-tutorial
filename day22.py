# 26/09/25
#-------------------------------------------------------------------

# static method

# class ABC:
#     @staticmethod
#     def greet(name):
#         print(f'Hello {name}')
#     def fun(self):
#         print('-------------------')
#         self.greet('Parker')
# obj=ABC()
# obj.greet('Peter')
# obj.fun()
# ===================================================
# class ABC:
#     @staticmethod
#     def greet(self,name):
#         print(f'Hello {name}')
#     def fun(self):
#         def fun1():
#             print('Inside')
#         fun1()
#         print('-------------------')
        # self.greet('Parker')
# obj=ABC()
# obj.greet('Peter') # it directly goes to self, not name
# obj.fun()
# o/p: TypeError: ABC.greet() missing 1 required positional argument: 'name'
#===============================

# class P_H:
#     value=8
#     def fun(self):
#         self.new='listen'
#         # print(self.value)
#         print(self)
#     @classmethod
#     def new_class(cls):
#         print(cls.value) # 8
#         # print(cls.new) # AttributeError: type object 'P_H' has no attribute 'new'
#         print(P_H) # <class '__main__.P_H'>
#         print(cls.value) # 8
# obj=P_H()
# obj.fun() # <__main__.P_H object at 0x00000270E3727BF0>
# obj.new_class() # AttributeError: type object 'P_H' has no attribute 'new'
# print(obj.new) # listen
#==========================
# import copy
# l=[100,150,200,350,[10,20]] # for in nested list it create another address 
# # l=[100,150,200,350]
# l1=copy.copy(l)
# # l1=l.copy()
# l1[4][1]=1000 # both the nested-list connected each other in one address
# print(l)
# print(l1)
# print(id(l))
# print(id(l1))
# print(id(l[0]))
# print(id(l1[0]))

# l=[1,50,20,30]
# l1=l
# l1[3]=100
# print(id(l))
# print(id(l1))
# print(id(l[0]))
# print(id(l1[0]))
# print(l)
# print(l1)
#=====================================================
import copy
s=[100,150,200,350,[10,20]]
s1=copy.deepcopy(s)
print(id(s))
print(id(s1))
print(id(s[0]))
print(id(s1[0]))
print(s)
print(s1)
s[0]=10
print(s)
print(s1)
s[4][0]=100
print(s)
print(s1)
s1[4][1]=500
print(s)
print(s1)
#================================================



