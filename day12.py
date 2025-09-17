# 13/09/25
# -------------------------------------------------------------------------------------

'''
    11. count() # returns integer // returns the occurance(frequency | count) of a character
        str_name.count(char)
        
    12. index() # returns int
        dtr_name.index(char)
        
    13. split() # returns list
        str_name.split(sep)
    
    14. join() # returns string
        .join(values)

    
    
'''

# s='py spiders btm'.split()
# print(''.join(s))

# 1
'''n='py spiders btm'.split()
print(n)
for x in range(len(n)):
    print(len(n[x]),end=' ')'''
# l=[len(l) for x in n]
# 2
'''n='py spiders btm'.split()
print(n)
k=''
l=[]
for x in range(len(n)):
    l.append(len(n[x]))
for x in range(len(n)):
    k+=n[x]+'-'+str(l[x])+' '
print(k)'''

# 3
'''n='py spiders btm'.split()
es=''
for i in range(len(n)):
    if i%2!=0:
        for x in range(-1,-len(n[i])-1,-1):
            es+=str(n[i][x])
        n[i]=es
print(n)'''

# 4
'''n='py spiders btm'.split()
ns=''
for x in range(len(n)):
    
    k=n[x]
    
print(k)'''



'''
user input:-
'py spiders btm'
1)
o/p:
[2,7,3]
2)
py-2 spiders-7 btm-3
3)
py sredips btm
4)
[py,ss,bm]
'''


# print("PY-Spiders BTM>all spiders".count('p'))
# print("py-spiders-BTM".index('p')) # output : 0
# print('py spiders btm'.split('')) // don't pass empty string
# print('py spiders btm'.split()) # output: ['py', 'spiders', 'btm']



# ----------------> Assignment <-------------------
#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# take string from user, split the words, convert upper case if the is even index otherwise lower, conbine all the values
'''n=input('Enter string : ')
words=[]
word=''
for x in n:
    if x!=' ':
        word+=x
    else:
        if word!='':
            words.append(word)
        word='''''


# n=input('Enter string : ')
# without using keyword & build-in method, check even or odd after that write on a single line 
'''n=int(input('Enter number :'))
res=['even','odd']
print(res[n%2])'''
# print('even' if int(input('Enter number :'))%2==0 else 'odd')

# without using build-in method & + operator, addition of two numbers
'''def  add(a,b):
    while b!=0:
        a+=1
        b-=1
    return a
print(add(10,5))'''


#  without using build-in method, preform split
'''s=input('Enter string : ')
words=[]
word=''
for x in s:
    if x!=' ':
        word+=x
    else:
        words.append(word)
        word=''
if word!='':
    words.append(word)
print(words)'''




# ----------------------------------------------------------
# factorial
'''f=1
n=6
for i in range(n,0,-1):
    f=f*i
print(f)'''

# factors of that number
#    perfect number // 6 --> 1+2+3 --> 6==n
# fibonacci series // is user enter n number then print the n number
# 
'''
nested loop
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
'''n=int(input('Enter number : '))
for x in range(n):
    for j in range(x+1):
        print(j+1,end=' ')
    print()'''