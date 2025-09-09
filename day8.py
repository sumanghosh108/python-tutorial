# 09/09/25
# ----------------------------------------------------------------------

# list comprehension --> in one line using for loop conditional statement
'''list=[]
n=eval(input('Enter: '))
for i in range(1,n+1):
    list.append(i)
print(list)'''

# l=eval(input([i for i in range(1,7)]))
# n=int(input('Enter:'))
# print([int(input('Enter element: ')) for i in range(1,int(input('Enter Number of Elements : '))+1)])
# print(l)
# print([i for i in range(1,int(input('Enter the last number : '))+1) if i%2==0])

# --------------> Tuple <---------------------------------------

# var=(val1,val2, ..., valn)
# var=val1,val2,...,valn
# var=value
'''a=10,
d=(100)
print(type(a))
print(d)
print(type(d))'''

'''a=10,20,23,45,55
a[3]=100
print(a) # TypeError'''

'''l=(i for i in range(1,10))
print(type(l)) # Output: generator
print(list(l)) # possible // Output: [1,2,3,4,5,6,7,8,9]'''

# print(i for i in (10,20,30,40,50))

# n=int(input())
# print(f'{n%2==0}')

a=['even','odd']
print(f'the entered value is {a[int(input('Enter number : '))%2]}')