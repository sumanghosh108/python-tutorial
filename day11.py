# 12/09/25
# -----------------------------------------------------------------------------------

'''
    8. dict_name.update({key:value,key:value,............}) # returns None
        d.update({'s_name1':100, 'new_key': 108}) // update single or multiple {key:value} pairs
        
    9. setdefault('key',value) # returns value
        res=d.setdefault('s_name1',100) // if the key present it's returning the corresponding value, 
        
    10. dict_name.get(key) # returns value if key present, else None or message pass by program
        res=d.get('new') // returns None
        res=d.get('new','key is not present') // print - key is not present
        res=d.get('s_name') // returns value of the key
        
    11. new_dict = {}.fromkeys(collection,default_value) # returns dict // it creats a dict with a default value for all the keys // collection --> list, tuple, dict
        l=['sandya','heer','batman','suman','dhanujaya']
        d={}.fromkeys(l) // assigning the value to None
        d={}.fromkeys(l,'present) // assiging the value to present
        d={}.fromkeys(l,['present','yes']) // assinging the value to ['present','yes']
        
'''



'''d={'s_name':['sandya','heer','batman','suman','dhanujaya'],
   's_marks':[95,94,100,95,95],
   'last':[1,2,3,4]
   }'''

'''l=['sandya','heer','batman','suman','dhanujaya']
d={}.fromkeys(l,['present','yes']) 
print(d)'''

# res=d.get('new')
# print(res,d)

# l=[value for loop]
# s={0,1,2,3,4,5} // id pass continuous order then store in order otherwise store in suffle order
# d={k:v for loop if condition} 


# l=['sandya','heer','batman','suman','dhanujaya']
# d={'sandya':6,'heer':4,'batman':6,'suman':5,'dhanujaya':9}
    
# d={k:len(k) for k in l}
# print(d) // output: {'sandya': 6, 'heer': 4, 'batman': 6, 'suman': 5, 'dhanujaya': 9}
    
    
'''d={k for k in range(10)}
print(d)''' 

# ---------------> Assignment <-----------------
# without using build-in method, perform update
'''dict_name.update({key:value,key:value,............}) # returns None
        d.update({'s_name1':100, 'new_key': 108})'''

'''d={'s_name':['sandya','heer','batman','suman','dhanujaya'],
   's_marks':[95,94,100,95,95],
   'last':[1,2,3,4]
   }
x=int(input('Enter number of keys : '))
for i in range(x):
    x=eval(input(f'Enter the Key :'))
    if type(x) not in [list,set,dict]:
        y=eval(input(f'Enter the Value : '))
        d[x]=y
    else:
        print('Invalid data types (this data type not supported for key) ❌❌❌ !!')
print(d)'''

# without using build-in method, setdefault
'''setdefault('key',value) # returns value
        res=d.setdefault('s_name1',100)'''

'''d={'s_name':['sandya','heer','batman','suman','dhanujaya'],
   's_marks':[95,94,100,95,95],
   'last':[1,2,3,4]
   }
if d:
    x=eval(input(f'Enter the Key :'))
    if type(x) not in [list,set,dict]:
        y=eval(input(f'Enter the Value : '))
        d[x]=y
        print(y)
    else:
        print('Invalid data types (this data type not supported for key) ❌❌❌ !!')
print(d)'''


#--------------------------------------------------------------------------------------------------
#                       ||||||||||||||||||||||||||||||||||||||||||
#                                    ||||||||||||
#                                        |||

# -----------------------------------------> String <-------------------------------------------
# collection of characters, enclosed with single '' or double ""
#--------------------------> Properties <-------------------
'''
    1. is a homogeneous collection
    2. ia a ordered collection
    3. support duplicate character
    4. support indexing and slicing
    5. is a immutable collection
    6. 
    
'''

'''s='pyspiders'
for i in s:
    print(i,end=' ')'''

# user entered input, print the consonent
'''n=input('Enter string : ')
count=0
for i in n:
    if i not in 'aeiouAEIOU':
        print(i,end=' ')
        count+=1
print()
print(count)'''
# reverse a sring without using build-in method
# n=input('Enter string : ')
'''for x in range(-1,-len(n)-1,-1):
    print(n[x],end='')'''

'''rev=''
for i in n:
    rev=i+rev # p+'' -> p | y+p -> yp | s+yp -> syp
print(rev)'''

# ---------------------> Build-in Methods <-------------------------------

'''
    s='PySpiders'
    
    1. upper() # returns string
        str_name.upper()
    2. isupper() # returnss boolean
        str_name.isupper()
    3. lower() # returns string
        str_name.lower()
    4. islower() # returns boolean
        str_name.islower()
    5. title() # returns a version of the string where each word is titlecased // first letter of each word convert to upper case and remaining char is lower case
        str_name.title()
    6. istitle() # returns boolean
        str_name.istitle()
    7. capitalize() # returns // make the 1sr char have upper case and rest lower case
        str_name.capitalize()
    8. isdecimal() # returns boolean
        str_name.isdecimal()
    9. isalpha() # returns boolean
        str_name.isalpha()
    10. isalnum() # returns boolean
        str_name.isalnum()
        
'''
'''s1='Ph'
s2='1234'
s3='1.56874'
s4='suman1'
# print(s.lower())
# print(s.islower())
print(s1.isupper())
print(s2.isupper())
print(s3.isupper())
print(s4.isupper())'''




# --------------> Assignment <---------------------------
# without using build-in method, upper | +32 or -32
'''upper() # returns string
        str_name.upper()'''
        
'''x=input('Enter string : ')
for i in x:
    if ord(i)>=97 and ord(i)<=122:
        i=chr(ord(i)-32)
        print(i,end='')'''

# without using build-in method, isupper
'''isupper() # returnss boolean
        str_name.isupper()'''

'''x=input('Enter string : ')
l=''
for i in x:
    if ord(i)>=65 and ord(i)<=90:
        l+=i
if len(l)==len(x):
    print('True')
else:
    print('False')'''



