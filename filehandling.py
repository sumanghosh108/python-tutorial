# open file
# file=open('example.txt','r')

# read file
# file=open('example.txt','r')
# content=file.read() # read entire data
# print(content)
# file.close()

# read one line 
# file=open('example.txt','r')
# content=file.readline() # read first line
# print(content)
# file.close()

# read line by line
# file=open('example.txt','r')
# content=file.readlines() # list entire data --> one line one item of the list
# print(content)
# file.close()

# write to a file
# file=open('example2.txt','w') # write mode -- over write
# file.write('Hello.., kaise ho')
# file.close()

# append
# file=open('example2.txt','a') # append mode --> incremental write
# file.write('\nAgain accha hu.')
# file.close()

# close a file
# using with statement
# with open('example2.txt','r') as file:
#     content=file.read()
#     print(content)



# -------
'''
    r+ : read and write
        -> the file pointer position at the bigining of the file.
        -> throws an error if file not exist.
        -> opens an existing file without truncating it.
        -> first perform read operation then write operation -> wrrite data to be added in the last position
        -> if first perform write operation then read operation ->>
                the data will be inserted at begining of the file ->>
                erase the same length of the input data, and rest are same ->>
                but only see the rest of the data, not able to see the entire data.
        use:
            -> if want to read data first and write(append) data to same file
    
    w+ : write and read
        -> the file pointer position at the begining of the file
        -> creates new file if file does not exist.
        -> opens an existing file and truncate it.(erase the previous data)
        -> after writing curser position at the last position.
        -> when perform write then read nothing is shown->>
                because after  writing the curser is in last position, after that nothing is present ->>
                -> if want to read the file, perform seek() operation after write operation->>
        use:
            -> when to write data and read the same data after writing
    
    a+ : append and read
        -> the file pointer position at the last.
        -> if file not present then create a new file then append to it.
        -> write the data atlast with the previous content.
        -> when perform read operation then write operation, it shows nothing ->>
                because the cursor is the last position ->>
                if perform write operation then read operation then also it shows nothing ->>
                -> if want to read the file, then need to perform seek() operation before reading.
                
    
'''

# with open('example2.txt','r') as file:
#     content=file.read()
#     print(content)

with open('data2.txt','a+') as file:
    # print(file.read())
    file.write('\nhello4')
    # print(file.read())
    file.write('\nhi4')
    # print(file.read())
    file.seek(0)
    data=file.read()
    print(data)
    

