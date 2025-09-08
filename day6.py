# 05/09/25
#---------------------------------------------------------------------------------------------------------------------------------
# reverse string char
'''s=input('Enter: ')
# rev_s=''
for i in range(len(s)-1,-1,-1):
    print(s[i],end='')
    rev_s=rev_s+s[i]
print(rev_s)'''

'''s=input('Enter: ')
rev=s[-1:-len(s)-1:-1]
for i in rev:
    print(i,end='')'''

# print number 10 to 20

'''s_value=10
while s_value<=20:
    print(s_value)
    s_value+=1'''

# take two int input & check the value div by both 3 & 8
'''a,b=int(input('Enter 1st num: ')),int(input('Enter 2nd num: '))
while a<=b:
    if a%3==0 and b%8==0:
        print(a)
    a+=1'''

'''bal=int(input('Enter balance:'))
while True:
    option=int(input('1.Withdraw\n2.Deposite\n3.Balance\nEnter option:'))
    match option:
        case 1:
            amt=int(input('Enter amount to withdraw: '))
            if amt>0 and bal>=amt:
                bal-=amt
                print(bal)
                break
        case 2:
            dep=int(input('Enter amount: '))
            if dep>0:
                bal+=dep
                print(bal)
                break
        case 3:
            print(bal)
            break
        case _:
            print('Invalid Option')'''

# ----> when not updating the start value it's running infinite time & when the condition is always true

# ---> break to stop the loop
'''start=10
while start <=18:
    if start == 15:
        break
    print(start)'''

# ---> continue to skip the value & give back to the loop
'''start=10
while start <=18:
    if start == 15:
        continue
    print(start)
    start+=1'''

# ---> pass to create to empty block
'''start=10
while start <=18:
    if start == 15:
        pass
    print(start)
    start+=1'''

# take 1 number & add only odd digit of that number
'''num=int(input('Enter num: '))
sum=0
while num>0:
    digit=num%10
    if digit%2!=0:
        sum+=digit
    num=num//10
print(sum)'''

# nested loop
# ---> range method
'''n=int(input('Enter num: '))
for i in range(n):
    for j in range(n):
        print(j,end='')
    print()'''

# Assinment --> Q.1. reverse the number using while loop -----------------------------------------
'''n=int(input('Enter num: '))
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print(rev)'''
# Q.2. count,sum,avg for input(multi value not using loop), check the number is even or odd using while loop ------------------
'''odd_count,even_count,sum,avg,n=0,0,0,0,int(input('Enter number: '))
while n>0:
    digit=n%10
    if digit%2!=0:
        print(digit,'Odd')
        odd_count+=1
    else:
        print(digit,'Even')
        even_count+=1
    sum+=digit
    total=odd_count+even_count
    avg=sum/total
    n=n//10
print('Odd Count:',odd_count,'Even Count:',even_count,'Sum:',sum,'Avg:',avg)'''

'''num=int(input('Enter num: '))
sum_odd,c_odd,sum_even,c_even=0,0,0,0
while n!=0:
    if n%2:
        dum_odd+=last_d
        c_odd+=1
    else:
        sum_even+=last_d
        c_even+=1
    n//=10
print(f'Sum of odd numbers: ')
print(f'Count of odd numbers: ')
print(f'Avg. of odd numbers: ')
print(f'Sum of even numbers: ')
print(f'Count of even numbers: ')
print(f'Svg. of even numbers: ')'''

# Assinment Q.3 ----------------------
'''1 2 3 4 5
    6 7 8 9 10
    11 12 13 14 15
    16 17 18 19 20
    21 22 23 24 25'''
#---------->
'''n=int(input('Enter num: '))
for i in range(n):
    for j in range(n):
        print(i*n+j+1,end=' ')
    print()'''

# Assinment Q.4 ------------------
'''@ * @ * @
    @ * @ * @
    @ * @ * @
    @ * @ * @
    @ * @ * @'''
#---------->
'''for i in range(5):
    for j in range(5):
        if j==0:
            print('@',end=' ')
        else:
            if j%2==0:
                print ('@',end=' ')
            else:
                print('*',end=' ')
    print()'''

# Assinment Q.5 --------------
'''#  ? ? ? ? ? 
    # # # # # # 
    # ? ? ? ? ?
    # # # # # #
    # ? ? ? ? ?'''
#---------->
'''for i in range(5):
    if i==0 or i%2==0:
        for j in range(5):
            print('?',end=' ')
        print()
    else:
        for j in range(5):
            print('#',end=' ')
        print()'''
# Assinment Q.6
'''Q.3, Q.4, Q.5 using while loop'''

#Q.3 -------------------->
'''1 2 3 4 5
    6 7 8 9 10
    11 12 13 14 15
    16 17 18 19 20
    21 22 23 24 25'''
#---------->
'''s_value=0
while s_value < 5:
    s_value2=0
    while s_value2 < 5:
        print(s_value*5+s_value2+1,end=' ')
        s_value2+=1
    s_value+=1
    print()'''
#Q.4 --------------->
'''@ * @ * @
    @ * @ * @
    @ * @ * @
    @ * @ * @
    @ * @ * @'''
#---------->
'''s_value=0
while s_value < 5:
    s_value2=0
    while s_value2 < 5:
        if s_value2 %2==0:
            print('@',end=' ')
        else:
            print('*',end=' ')
        s_value2+=1
    s_value+=1
    print()'''

# Assinment Q.5 --------------
'''#  ? ? ? ? ? 
    # # # # # # 
    # ? ? ? ? ?
    # # # # # #
    # ? ? ? ? ?'''
#--------->
s_value=0
while s_value<5:
    s_value2=0
    if s_value%2==0:
        while s_value2<5:
            print('?',end=' ')
            s_value2+=1
    else:
        while s_value2<5:
            print('#',end=' ')
            s_value2+=1
    s_value+=1
    print()
    

#-------------------------------------------------------------------------------------------------------------------
'''s_value=0
while s_value<=5:
    s_value2=0
    while s_value<=5:
        print('*',end='')
        s_value2 +=1
    s_value+=1'''
    

