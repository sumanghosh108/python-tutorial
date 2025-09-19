# 11/09/25
# --------------------------------------------------------------

# Tuple comprehension is not possible   
'''t=(1 for i in range(10))
for i in t:
    print(i)'''
    
'''t=(0,[1,2,3])
t[1][2]=1000 # possible bcz modify the list
print(t) # output: 0,[1,2,1000]'''

'''t=(1,2,3)+(4,5,6)
print(t)'''

'''s={1,2,3}
new={int(input())}
s|=new
print(s)'''

'''s={x for x in range(10)if not x%2}
print(s)'''

'''c='helloo'
s={x for x in c if x in 'aeiouAEIOU'}
print(s)'''

# for loop range not support in set # output: TypeError: 'set' object is not subscriptable
'''s={1,2,3,4}
for i in range(len(s)):
    print(s[i])'''
# -------------------> dictionary <---------------------------
# group of key value pairs seperated by comma, enclosed with curly brackets
# d={} # empty dictionary
# ------------------> properties <--------------------
'''
    1. homogeneous and hetrogeneous
    2. ordered collection
    3. doesn't support indexing and slicing
    4. keys can be immutable data types (int, float, complex, boolean, sring, tuple)
    5. values can be any data types
    6. key should be unique
        d={(1,2,3,):100,'hhhh':100, 's':100,'s':200}
        print(d) # output: {(1, 2, 3): 100, 'hhhh': 100, 's': 200}
    7. is a mutable collection
'''
'''
    - to get a value from a dictionary
        dictionary_name[key]
    - update a value to a dictionary
        dictionary_name[key]=new_value
    - 
'''

'''d={(1,2,3,):100,'hhhh':100, 's':100,'s':200}
d['hhh'] = 5
d[5]='kkk'
print(d)'''

# enter one number, i.e key_value_pair , values, print the dictionary

'''d={}
n=int(input('Enter number of keys: '))
for i in range(n):
    x=eval(input(f'Enter the Key {i+1} :'))
    if type(x) not in [list,set,dict]:
        y=eval(input(f'Enter the Value {i+1}: '))
        d[x]=y
    else:
        print('Invalid data types (this data type not supported for key) ❌❌❌ !!')
print(d)'''

'''s=eval(input())
if type(s)==int:
    print('True')'''
    

# d={'s_name':['sandya','heer','batman','suman','dhanujaya'],'s_marks':[95,94,100,95,95]}
# print(d) # output: {'s_name': ['sandya', 'heer', 'batman', 'suman', 'dhanujaya'], 's_marks': [95, 94, 100, 95, 95]}

# ------------> build-in methods ,-------------------
    # 1- .items()
    #   dict_name.items() # returns list of tuple
        
        # for i in [('s_name', ['sandya', 'heer', 'batman', 'suman', 'dhanujaya']), ('s_marks', [95, 94, 100, 95, 95])]:
        #     print(i) # output: ('s_name', ['sandya', 'heer', 'batman', 'suman', 'dhanujaya'])
        #                         # ('s_marks', [95, 94, 100, 95, 95])

        # for i,j in [('s_name', ['sandya', 'heer', 'batman', 'suman', 'dhanujaya']), ('s_marks', [95, 94, 100, 95, 95])]:
        #     print(i,j) # output:  s_name ['sandya', 'heer', 'batman', 'suman', 'dhanujaya']
        #                         # s_marks [95, 94, 100, 95, 95]

        # for i,j,z in ('s_name', ['sandya', 'heer', 'batman', 'suman', 'dhanujaya'],100), ('s_marks', [95, 94, 100, 95, 95]):
        #     print(i,j,z)

        # for i in d.items():
        #     print(i) # output: ('s_name', ['sandya', 'heer', 'batman', 'suman', 'dhanujaya'])
        #                         # ('s_marks', [95, 94, 100, 95, 95])

        # for key,value in d.items():
        #     print(key,value) # output: s_name ['sandya', 'heer', 'batman', 'suman', 'dhanujaya']
        #                                 # s_marks [95, 94, 100, 95, 95]

        # for key,value,pair in d.items():
        #     print(key,value,pair)
    
    # 2- dict_name.keys() # returns dict_keys
    # 3- dict_name.values() # returns dict_values
    # 4- result=dict_name.copy() # returns dictionary
    # 5- dict_name.clear() # retrurn Nonn
    # 6- result = dict_name.pop(key) # returns key values
    # 7- result = dict_name.popitem() # returns tuples // removes the last key

# res=d.pop('s_name1','key is not present')
'''res=d.popitem()
print(res,d)'''

# ---------> assignment <---------------
# without using build-in method, pop in dictionary | use del
'''d={'s_name':['sandya','heer','batman','suman','dhanujaya'],
   's_marks':[95,94,100,95,95],
   'regd_no':[2101201010,2101201021,2101201051,2101201098,2101202145]
   }
pop_item=input('Enter the key want to pop: ')
if pop_item in d:
    del d[pop_item]
    print(f'After deleting {pop_item}, the remaining dictionary {d}')
else:
    print(f'Entered item {pop_item} not present in dictionary')'''



# without using build-in method, popitem() in dictionary | use del
'''d={'s_name':['sandya','heer','batman','suman','dhanujaya'],
   's_marks':[95,94,100,95,95],
   'regd_no':[2101201010,2101201021,2101201051,2101201098,2101202145]
   }
if d:
    for key in d:
        last_key=key
    del d[last_key]
    print(f'popitem : {last_key}')
    print(f'Remaining items: {d}')'''


'''d={'s_name':['sandya','heer','batman','suman','dhanujaya'],
   's_marks':[95,94,100,95,95],
   }'''
'''c,l,k=1,len(d),''
for i in d:
    if c==l:
        k=i
    c+=1
print(k,d[k])
del d[k]
print(d)'''

'''last_key=[i for i in d][-1]
print(last_key,d[last_key])
del d[last_key]
print(d)'''

