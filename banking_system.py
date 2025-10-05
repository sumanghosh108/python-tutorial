# Banking System using inheritance properties
# -----------------------------------------------------------------

#base class / super class
class AccountHolder:
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    def get_balance(self):
        print(f'Account holder name : {self.name}, balance : {self.balance}')
#single inheritence --> Sav_Account(child) inherits from AccountHolder(super class)
class Sav_Account(AccountHolder):
    def deposite(self,amt):
        self.balance+=amt
        print(f'{self.name}, balance after deposite : {self.balance}')
    def withdraw(self,amt):
        if amt<=self.balance:
            self.balance-=amt
            print(f'{self.name}, amount after withdraw : {self.balance}')
        else:
            print(f'current amount : {self.balance}')
#multilevel inheritance --> Pre_Sav_Account(child) inherits from Sav_Account(parent) -> Sav_Account(parent) inherit from AccountHolder(super)
class Pre_Sav_Account(Sav_Account):
    def add_interest_daily(self):
        interest=self.balance*0.01
        self.balance+=interest
        print(f'premium saving account amount : {self.balance}')
#hierarchical inheritance --> [Curr_Account, Loan_Account, Fix_Account](multiple-child) inherit from AccountHolder(parent)
class Curr_Account(AccountHolder):
    def role(self):
        print('Current Account Holder')
class Loan_Account(AccountHolder):
    def get_loan(self,amt):
        self.balance+=amt
        print(f'Loan amount : {amt}, total balance : {self.balance}')
class Fix_Account(AccountHolder):
    def fixed_dep(self,amt):
        self.balance+=amt
        print(f'fixed deposite amount : {amt}, total amount : {self.balance}')
#multiple inheritance --> Dig_Customer(child) inherite [On_Banking,Mob_Banking](multiple-parent)
class On_Banking:
    def on_service(self):
        print('internet banking')
class Mob_Banking:
    def mob_service(self):
        print('mobile banking')
class Dig_Customer(On_Banking,Mob_Banking):
    def role(self):
        print('Digital Customer')
#hybrid inheritance --> combination of multilevel, hirearchical, multiple
class BankManager(Pre_Sav_Account,Curr_Account,Dig_Customer):
    def role(self):
        print('bank manager')

# -------------
# savings=Sav_Account('Sum',50000) # object of single
# savings.get_balance()
# savings.deposite(10000)
# savings.withdraw(2000)
premium=Pre_Sav_Account('Sum',50000) # object of multilevel
premium.add_interest_daily()
premium.deposite(200)
premium.withdraw(100)
# current=Curr_Account() # object of hierarchical
# current.role()
# Loanaccount=Loan_Account() # object of hierarchical
# Loanaccount.role()
# Fixeddeposite=Fix_Account() # object of hierarchical
# Fixeddeposite.role()
# digitalcustomer=Dig_Customer() # object of multiple
# digitalcustomer.role()
# digitalcustomer.on_service()
# digitalcustomer.mob_service()
# bankmanager=BankManager() # object of hybrid
# bankmanager.role()
# bankmanager.on_service()
# bankmanager.mob_service()