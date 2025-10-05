# 27/09/25
# -------------------------------------------------------------------


try:
    def calculator(a,b):
        while True:
            option=int(input('Enter option : 1.add, 2.subtraction, 3.multiplication, 4.division'))
            # operator=input()
            match option:
                case 1:
                    print(a+b)
                case 2:
                    print(a-b)
                case 3:
                    print(a*b)
                case 4:
                    print(a/b)
                case _:
                    print('Invalid Option')
                    continue
            break
    a=int(input('Enter number 1 : '))
    b=int(input('Enter number 2 : '))
    calculator(a,b)
except Exception as e:
    print('Error',e)
except ValueError as e:
    print('Error',e)
except ZeroDivisionError as e:
    print('Error',e)
# except Exception as e:
#     print('Error',e)
