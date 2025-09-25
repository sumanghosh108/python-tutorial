from .file1 import Payment # relative import // by using dot(.)
# from main.file2 import Payment # absolute import // actual path

class UPI(Payment):
    # concrete method
    def pay1(self):
        print('Welcome to UPI payment .......')
    # concrete method
    def pay2(self):
        print('Option 2 .......')
        super().pay2() # ❌❌❌❌
        
obj=UPI()
obj.pay2()