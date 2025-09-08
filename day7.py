# 08/09/25
# ----------------------------------------------------------------------

# --------> Collections  <------------------------
'''
    -List \\ list()
        listname = [val1,val2,.....,valn] group of values, saparated by comma(,), and enclosed within square brackets[]
        1. l=list(input()) ------> take as string, give back one-by-one character
        2. eval() ---> to take any data type // mainly use in collections
            ---> Properties <-------------------------------------------------------------------
            1. list is a both homogeneous and heterogeneous collections
                l=[1,2,3,4,5] --> homogeneous
                l=[1,2,6,10.5,'Hello'] --> hetero
            2. is an ordered collection
            3. supports duplicate values
                l=[1,2,2,3,2]
            4. supports indexing(+ve & -ve)
                1. to get a value 
                    l[3] --> to get 4th value
                2. to update a value by using index
                    l[2]=100 --> replacing the 3rd value with 100
            5. Supports slicing 
                l=['Hello','hi',1,2,100,4,46,78]
                print(l[2:5])
                print(l[-7:-3])
                l=['Hello','hi',1,2,100,4,46,78]
                l[0:5]=[25,1000,5000,'BYE'] ----> update multiple value
            6. is a mutable collection(add, replace, remove)
                l=[10,11,18,25,7,333]
                l=l+[100] --> using concating two list # output:10,11,18,25,7,333,100
                del l[4] / del l ---> using keyword 'del' remove the item or entire list
                
        3. Build-in method -------------------------------------------------------------------
            1. .copy() --> returns a shallow copy of a list 
                l=[1,2,3,10,50]
                copy_list=list.copy()
                copy_list[1]=100
            2. .clear() ---> returns empty list
                l=[1,2,3,10,50]
                list.clear() // output:[]  --> returns an empty list
            3. .append(value) --> returns None
                l=[1,2,3,10,50]
                list.append(100) // output:[1,2,3,10,50,100]
            4. .insert(index,value) --> returns type None
                list.insert(index,value) -->  +ve out-of range, add it to last & -ve out-of range, add it to first
            5. .extend --> returns None
                list.extend(collection) --> // appending the elements by iterable
            5. .index(value) --> returns the index of the first occurance of the list 
                l=[1,2,3,10,50,'python']
                ind=list.index('python') // output:5
                ind=list.index('50') // output:ValueError --> 50 is not in the list
            6. .remove(value) --> // returns type None // remove one value at a time
                l=[1,2,3,10,50,'python']
                list.remove(10) // output:[1,2,3,50,'python']
            7. .pop(index) --> returns value(removed element) // pass an index // default index is -1 
                list.pop(index_of_the_value)
            8. .count(value) --> returns an integer // how many times a particular value present 
                list.count(value) // if value not present it returns 0
            9. .reverse() --> returns None //reverse the list
                list.reverse()
            10. .sort() --> returns None //sort the collection in ascending order // default is ascending
                list.sort() // ascending order
                list.sort(reverse=True) // descending order





    -Tuple
    -Set
    -Dictionary
'''
'''l=list(input('Enter the values: '))
print(l,type(l))
print(list('[12345,123]'))'''

'''l=eval(input('Enter: '))
print(l,type(l))'''


'''l=['css','sql','python']
l.sort()
l.sort(reverse=True)
print(l)'''

# --------------------> Assignment <---------------------
# without using build-in , count how many times the value is present
# without using build-in , pop, remove, index // pop & remove 'del' | for loop range method
# without using build-in reverse 
# write the syntax & return type for all the build-in methods

# ---------> Count how many times the element present in a list <------------------------
'''l=[1,2,3,4,5,7]
count=0
for i in l:
    count+=1
print(count)'''

# ---------> Pop an element from a list <-----------------------
'''l=[1,2,5,8,10,15,17]
n=int(input('Enter the index : '))
if n>0: # for positive indexing
    for i in range(len(l)):
        if i==n:
            del l[i]
            break
else: # for negative indexing
    for i in range(-1,-len(l)-1,-1):
        if i==n:
            del l[i]
            break
print(l)'''

# -------> Remove an item from a list <--------------------
'''l=[1,2,5,8,10,15,17]
n=int(input('Enter the value : '))
for i in range(len(l)):
    if l[i]==n:
        del l[i]
        break
print(l)'''

# ------> Find an index <------------------------
'''l=[1,2,5,8,10,15,17]
n=int(input('Enter the value : '))
for i in range(len(l)):
    if n == l[i]:
        print(i)'''

# -------> Reverse an list <-------------------------
'''l=[1,2,5,8,10,15,17]
print(l)
reverse_list=[]
for i in range(-1,-len(l)-1,-1):
    reverse_list+=[l[i]]
print(reverse_list)'''

