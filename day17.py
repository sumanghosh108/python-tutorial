# 19/09/25
# --------------------------------------------------------------------------------------------

# Single level Inheritance : 
'''class trainer: # parent class
    def __init__(self):
        self.trainer_name='Trainer1'
        self.syllabus='python'
        self.programs='Pattern'
    def practical(self):
        print(f'Syllabus : {self.syllabus}\nPrograms : {self.programs}')
class student1(trainer): # child class
    def class_details(self):
        print(self.syllabus) # inheriting thr properties from parent
        print(self.programs)
    
s1=student1() # object of child class
s1.class_details()
s1.practical()
s1.practical1() # AttributeError: 'student1' object has no attribute 'practical1'
'''

# -----------
'''class Company:
    def __init__(self):
        self.employee_name='manager1'
        self.employee_level='Senior Manager'
        self.employee_id='4r8393yr3'
    def details(self):
        print(f'Manager name : {self.employee_name}\nManager level : {self.employee_level}\nManger ID : {self.employee_id}')
        print(self)
class Employee(Company):
    def emp_details(self):
        print(self.employee_name)
        print(self.employee_level)
        print(self)

get_details=Employee()
get_details.emp_details()
get_details.details()
'''
# -------------
'''class parent:
    def __init__(self,p_name,p_age):
        self.p_name=p_name
        self.p_age=p_age
class child(parent):
    def __init__(self,c_name,c_age,p_name,p_age):
        super().__init__(p_name,p_age)
        self.c_name=c_name
        self.c_age=c_age
c1=child('child1',2,'parent1',55)
print(c1.p_name,c1.p_age)
'''

# ---------
# Multi level inheritance
'''class Manager:
    def __init__(self):
        self.m_name='Thanos'
        self.m_id='T1234'
        self.m_salary='100L'
        self.project='Bank'
    def m_display(self):
        # print(self)
        print('Manager here !!!!')
        print(self.TL_name)
class TL(Manager):
    def __init__(self):
        super().__init__()
        self.TL_name='Robert'
        self.tl_id='R123'
        self.tl_sal='80L'
        self.domain='Full stack(django) and DA(python,PowerBI,Excel,SQL)'
    def display_TL_details(self):
        print(self.TL_name,self.tl_id,self.tl_sal,self.domain)
class EMP(TL):
    def __init__(self):
        super().__init__()
        self.emp_name='Ram'
        self.id='R123'
        self.sal='10L'
        self.assigned_work='Task1'
        self.assigned_by=self.TL_name
        self.p_manager=self.m_name
    def display(self):
        print(f'Emp name : {self.emp_name},Emp ID : {self.id},Emp salary : {self.sal},assigned work : {self.assigned_work},Assigned By ; {self.assigned_by},self.p_manager')
        # print(self)
        # super().display_TL_details()
        self.display_TL_details()
        self.m_display()
emp1=EMP()
emp1.display()
# emp1.m_display()
# emp1.display_TL_details()
# print(emp1.m_name)
'''
# Multiple Inheritance :
'''class t_python: # superclass1
    pass
class t_sql: # superclass2
    pass
class suman(t_python,t_sql): # baseclass(superclass1,superclass2)
    pass'''
    
'''class trainer1:
    def __init__(self):
        self.t_subject='python'
    def display(self):
        print(self.t_subject)
class trainer2:
    def __init__(self):
        self.t_subject='sql'
    def display(self):
        print(self.t_subject)
    def display1(self):
        print('Trainer 2 here..')
class student1(trainer1,trainer2):
    def __init__(self):
        super().__init__()
    def display(self):
        super().display()
suman=student1()
suman.display() # check first superclass then return
suman.display1() # if not paresent in first superclass then goes to second superclass
# suman.display2() # if not paresent then AttributeError
'''


# ---> Assignment <---------
'''create two parent class
1. perfect number
2. Reverse number
child
1. number // use this child class to get input and pass it to parent classes using super
create one method 
    - ask options from user // using match
    if user enters 1 - call perfectnumber()
    if user enters 2 - call reverse number() // display to user that number
'''
