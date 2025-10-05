'''
    1. Register (try block)
        user name
        password
        confirm password
        -> check length of username
            if 10 ask password and confirm password
            if both password not same , raise custom error exception
    2. if no error in try block
        else block
            print->Register seccussfully
    
'''
'''class PasswordError(Exception):
    pass
try:
    username=input('Enter user name : ')
    if len(username)>=10:
        password=input('Enter password : ')
        conf_password=input('Enter conf1irm password : ')
        if password != conf_password:
            raise PasswordError('password not match')
except PasswordError as e:
    print('Error',e)
except Exception as e:
    print('Error',e)
else:
    print('Register successfully')
'''
# custom default error --> by constructor chaining --> pass one parameter & some message
#                           --> when raise an error it will print default message
#                           --> if pass a message through raise, it override the default message
class PasswordError(Exception):
    def __init__(self,error='Default Error'):
        super().__init__(error)
            
try:
    raise PasswordError('New error')
    username=input('Enter user name : ')
    if len(username)>=10:
        password=input('Enter password : ')
        conf_password=input('Enter conf1irm password : ')
        if password != conf_password:
            raise PasswordError('password not match')
except PasswordError as e:
    print('Error: ',e)
# except Exception as e:
#     print('Error',e)
else:
    print('Register successfully')
    
