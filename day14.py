# 16/09/25
# --------------------------------------------------------------------------------

'''
1. global scope
2. local scope
'''

'''def fun(a,b):
    print(a,b)
fun(2,3)'''

# Global variable : we can access a veriable any where in the program (inside the block and outside the block)
'''s=7070
def fun():
    print(s,'fun')
fun()
def fun1():
    fun()
    print(s,'fun1')
fun1()'''

# Local variable : we can acess only inside, outside is not possible
'''s=500
def listen():
    s=100
    print(s)
print(s)
listen()
print(s)'''

# global keyword: by using global keyword we can declare a variable to global
'''s=500
def py_preminum():
    # b=1000
    # global s
    s=100
    print(s)
    # print(locals())
py_preminum()
print(s)
print(locals())'''

# -> local methods: this method should access only inside the function
#                   if we access outside the function it's acts as a global methods
# -> globals methods: this method returns all build-in variables & methods in the form of dictionary
#                   it returns user definr function & it's address, variable name & value


'''res = py_preminum # storing the address of py_preminum
res()'''
'''res = py_preminum # storing the address of py_preminum
res1=res
res()
res1()'''

# perfect number -> 1+2+3==6 == n
# perfect number 1 to 10000, by using for loop & function
'''
1. create a function 
    it should return True or False based on perfect number logic
2. by using forloop generate a number from 1 - 10000
    check by using if keyword
    next to if jusr call the function
    and function will return True or False
    if True store in a list
'''
'''l=[]
def is_perfect(num):
    total=0
    for x in range(1,num):
        if num%x==0:
            total+=x
    return total==num
for i in range(1,10000):
    if is_perfect(i):
        l.append(i)
print(l)'''

# 
'''
Class: 
'''
class myself:
    print('k')
# print(dir(myself))
print(len(dir(myself))) # output: 27 // version 3.12.5

