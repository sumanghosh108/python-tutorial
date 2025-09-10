# 10/09/25
# ------------------------------------------------------------------------------

# -------------> Tuple <-------------------------------
# tuple Build-in Method
'''
    1. tuple.count(value) # returns integer
        t1=(10,20,30,40,50,10)
        t1.count(10) # Output: 2
    2. tuple.index(value,start:0, stop;max_size) # returns integer
        t1.index(10) # Output: 0
        t1.index(10,1)
        t1.index(10,2,6)
'''

#--------------------> set <---------------------------------
# group of elements, seperated by comma(,) and enclosed with {} is called set.
'''
s1={10,20,30,40,50}
s2=set() # empty set
'''
# --------------------> Properties <-----------------------------
'''
    1. Can be homogeneous and hetrogeneous
    2. sets are unordered collection
        s1={20,3.4,10,500,30,40}
        print(s1) # Output: {3.4,20,500,40,30,10}
    3. Doesn't supports duplicate elements
        s1={10,20,10,10} # Output: {10,20}
    4. Doesn't support indexing 
        print(s1[0]) # TypeError: 'set' object is not subscriptable
    5. doesn't support slicing
    6. set is mutable collection
    7. set support int, float, complex,boolean, string, tuple as element
        s1={10,34,(1,2),[4,5]} # output: TypeError: unhashable type: 'list'
'''

# --------------> set comprehension <----------------
'''
set comprehension possible. # 
s1={x for x in range(1,11)} # output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
'''

# -----------> build-in methods <----------------------------
'''
    1. set.add(element) # returns None
        s1={10,20,30,40,50}
        s1.add(60) # Output: {10, 20, 30, 40, 50, 60}
    2. set.clear() # returns None
        s1={10,20,30,40,50}
        s1.clear() # Output: set()
    3. set.copy() # returns a shallow copy of set
        s1={10,20,30,40,50}
        s2=s1.copy() # Output: {10, 20, 30, 40, 50}
    4. set.difference(set) # returns a new set
        s1={10,20,30,40,50}
        s2={30,40,50,60,70}
        res=s1.difference(s2) # Output: {10, 20}
    5. set.difference_update(set) # returns None
        s1={10,20,30,40,50}
        s2={30,40,50,60,70}
        s1.difference_update(s2) # Output: {10, 20}
    6. set.discard(element) # returns None // if the value not present just ignore
        s1={10,20,30,40,50}
        s1.discard(10) # Output: {20, 30, 40, 50}
    7. set.intersection(set) # returns a new set // only common value
        s1={10,20,30,40,50}
        s2={40,50,60,70}
        res=s1.intersection(s2) # Output: {40, 50}
    8. set.intersection_update(set) # returns None // only common value
        s1={10,20,30,40,50}
        s2={40,50,60,70}
        s1.intersection_update(s2) # Output: {40, 50}
    9. set.isdisjoint(set) # returns boolean
        s1={10,20,30,40,50}
        s2={40,50,60,70}
        s1.isdisjoint(s2) # Output: False // common element present
        s2.isdisjoint(s1) # Output: False
    10. set.issubset(set) # returns boolean
        s1={10,20,30,40,50}
        s2={10,20}
        s1.issubset(s2) # Output: False
        s2.issubset(s1) # Output: True
    11. set.issuperset(set) # returns boolean
        s1={10,20,30,40,50}
        s2={10,20}
        s1.issuperset(s2) # Output: True
        s2.issuperset(s1) # Output: False
    12. set.pop() # returns any random element // pop form empty set --> KeyError
        s1={10,20,30,40,50}
        s1.pop() # Output: 10  
    13. set.remove(element) # returns None
        s1={10,20,30,40,50}
        s1.remove(10) # Output: {20, 30, 40, 50}
    14. set.symmetric_difference(set) # returns a new set // only unique value
        s1={10,20,30,40,50}
        s2={30,40,50,60,70}
        res=s1.symmetric_difference(s2) # Output: {10, 20, 60, 70}
    15. set.symmetric_difference_update(set) # returns None // only unique value
        s1={10,20,30,40,50}
        s2={30,40,50,60,70}
        s1.symmetric_difference_update(s2) # Output: {10, 20, 60, 70}
    16. set.union(set) # returns a new set
        s1={10,20,30,40,50}
        s2={30,40,50,60,70}
        res=s1.union(s2) # Output: {10, 20, 30, 40, 50, 60, 70}
    17. set.update(set) # returns None
        s1={10,20,30,40,50}
        s2={30,40,50,60,70}
        s1.update(s2) # Output: {10, 20, 30, 40, 50, 60, 70}
'''

# s1={x for x in range(1,11)}
# print(s1)

# -------------> List concatination <----------------------
'''
l1=[11,22,33,44,55]
l2=[66,77,88,99,100]
l3=l1+l2
print(l3) # Output: [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
l4=l1*3
print(l4) # Output: [11, 22, 33, 44, 55, 11, 22, 33, 44, 55, 11, 22, 33, 44, 55]
'''

