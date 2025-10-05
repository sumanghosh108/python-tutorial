# 29/09/25
# file=open('placement.txt','x')
# 
'''file=open('placement.txt','r') # if present then read the content, if not then --> FileNotFoundError
cursor=file.tell()
print(cursor)
file.read()
cursor=file.tell()
print(cursor)
# print('content:\n',content)
file.close()
'''

'''file=open('placement.txt','r+') 
cursor=file.tell() # returns int
print(cursor)
file.write('123456') # replace the existing content
cursor=file.tell()
print(cursor)
# print('content:\n',content)
# file.close()'''


file=open('placement.txt','r+') # if file exist  
cursor=file.seek(2) # from that possition 
file.write('000content111')
# print(cursor)
# cursor=file.tell()
# print(cursor)