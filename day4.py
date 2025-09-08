# num=int(input())
# n = num % 10
# if n == 5:
#     print("Batman")
# else:
#     print(n)

# take 1 char from user side , if uppercase print yes
# c = input()
# if char.isupper():
#     print("yes")
# else:
#     print("no")
# print(ord('A'),ord(c),ord('Z'))
# print(ord(c) >= 65 and ord(c) <=90)
# c=input()
# if c>='A' and c<='Z':
#     print('Uppercase')
#     print(chr(ord(c)+32))
# elif c>='a' and c<='z':
#     print('Not Uppercase')
#     print(chr(ord(c)-32))
# else:
#     print("Not an alphabet ")
# c=input()
# if (c>='A' and c<='Z') or (c>='a' and c<='z'):
#     if c in 'AEIOUaeiou':
#         print("Vowel")
#     else:
#         print("Consonant")
# elif c>='0' and c<='9':   
#     print("Digit")
# else:
#     print("Spl Char")
# c=input()
# asci_val=ord(c)
# if 65 <= asci_val <=90 or 97 <= asci_val <=122:
#     if c in 'AEIOUaeiou':
#         print("Vowel")
#     else:
#         print("Consonant")
# elif 48 <= asci_val <=57:
#     print("Not an alphabet")
# else:
#     print("Special character")

# num is divisible 8,7,3 print yes
# num=int(input())
# if num%8==0 or num%7==0 or num%3==0:
#     print("yes")
# else:
#     print("no")
#check the char is
# a = int(input())
# if a == 1:
#     print('Ironman')
# elif a == 2:
#     print('Captain America')
# elif a ==3:
#     print('Heeman')
# elif a == 4:
#     print('Thor')
# else:
#     print('Hulk')

# check single ,double, triple digit
# num=int(input())
# if num == 0:
#     print("Zero")
# elif num>=-9 and num<=9:
#         print("Single digit")
# elif (num>=10 and num<=99) or (num>=-99 and num<=-10):
#             print("Double digit")
# elif (num>=100 and num<=999) or (num>=-999 and num<=-100):
#         print("Triple digit")
# else:
#         print(" More then Triple digit")

# 
# num=int(input())
# if num%7==0:
#     if num%4==0:
#         print('div by both 7 and 4')
#     else:
#         print('div by 7 not by 4')
# else:   
#     if num%4==0:
#         print('div by 4 not by 7')
#     else:
#         print('not div by both 7 and 4')
# take 1 char from user side , if alpha 

# option=int(input())
# match option:
#     case 1:
#         print('Ironman')
#     case 2:
#         print('Captain America')
#     case _:
#         print('Invalid Option')
        
option=int(input())
balance=10000
match option:
    case 1:
        w_balance=int(input())
        if (w_balance <= balance) and (w_balance>0):
            balance=balance-w_balance
            print(balance)
        else:
            print("Insufficient Balance")
    case 2:
        d_balance=int(input())
        if d_balance <= 5000:
            balance = balance + d_balance
            print(balance)
        else:
            print("Limit Exceeded")
    case 3:
        print(balance)

