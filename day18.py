# 22/09/25
# ---------------------------------------------------------------------------------------

# Hierarchical Inheritance
'''class py_trainer:
    def subject(self):
        print('Python core','python advance','numpy pandas','ML')
    def t_experience(self):
        print('2+ years')
class mohan(py_trainer):
    def course_details(self):
        print('Premium PYTHON DA')
    def skills3(self):
        print('DA')
class suman(py_trainer):
    def course_details(self):
        print('Premium PYTHON DA')
    def skills2(self):
        print('python')
class reena(py_trainer):
    def course_details(self):
        print('Premium PYTHON DA')
    def skills1(self):
        print('sql')

obj=reena()
# obj.skills1()
# obj.t_experience()
obj1=suman()
obj1.skills2()'''

'''class Cric:
    def format(self):
        print('test','odi','t20','t10','ipl')
    def place(self):
        print('chinnaswamy','dubai','chepauk','nm stadium','Oval')
class Team1(Cric):
    def t_name(self):
        print('IND','PAK','SA','AFG','WI')
class Team2(Cric):
    def t_name2(self):
        print('NZ','ENG','AUS','BAN','IRK')
class tropy(Team1,Team2):
    def match_winner(self):
        print('Congratss!!')
        
obj=tropy()'''
# obj1=tropy()
# obj.format()
# obj.t_name2()
# print(obj)
# print(tropy.mro()) # set the order 
# print(obj1)

# class Laptop:
#     def __init__(self,color):
#         self.color=color
# obj1=Laptop('Black')
# print(obj1.color)


'''class One:
    pass
class two:
    pass
class three(One,two):
    pass
class four(two,One):
    pass
class five(four,three):
    pass
obj=five()
print(obj)
print(five.mro())'''


'''class One:
    pass
class two:
    pass
class three(One,two):
    pass
class four(One,two):
    pass
class five(four,three):
    pass
obj=five()
print(obj)
print(five.mro())'''


class B:
    pass
class A(B):
    pass
class C(B):
    pass
class D(C,A,B):
    pass

obj=D()
print(D.mro())
# 
# class B:
#     pass
# class A(B):
#     pass
# class C(B,A):
#     pass
# class D(C,A,B):
#     pass

# obj=D()
# print(D.mro())

# 