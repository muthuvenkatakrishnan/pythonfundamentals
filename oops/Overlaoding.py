# Overloading is not possible with respect to constructors and methods in Python
class Bank:

    def login(self,username, password, captcha):
        print("Yay you are logged in and your account balance is 50 million Crores")
    def login(self,mpin):
        pass
    def login(self,card,pin):
        print("Yay you are logged in and your account balance is 50 million Crores but 70% will be deducted as tax")

canara = Bank()
canara.login(8767)

sbi = Bank()

hdfc = Bank()

