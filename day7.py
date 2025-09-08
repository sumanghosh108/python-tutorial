# 08/09/25
# ----------------------------------------------------------------------

# --------> Collections  <------------------------
'''
    -List \\ list()
        listname = [val1,val2,.....,valn] group of values, saparated by coma(,), and enclosed within square brackets[]
        1. l=list(input()) ------> take as string, give back one-by-one character
        2. eval() ---> to take any data type // mzinly use in collections
            ---> Properties <-----
            1. list is a both homogeneous and heterogeneous collections
                l=[1,2,3,4,5] --> homogeneous
                l=[1,2,6,10.5,'Hello'] --> hetero
            2. is an ordered collection
            3. supports duplicate values
                l=[1,2,2,3,2]
            4. supports indexing(_ve & -ve)
                1. to get a value 
                    l[3] --> to get 4th value
                2. to updat a value by using index
                    l[2]=100 --> replacing the 3rd value with 100
    -Tuple
    -Set
    -Dictionary
'''
'''l=list(input('Enter the values: '))
print(l,type(l))
print(list('[12345,123]'))'''

'''l=eval(input('Enter: '))
print(l,type(l))'''
