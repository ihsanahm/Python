class BelanceException(Exception):
    pass




class BankAccount:
    def __init__(self, initialAccount, accName):
        self.belance=initialAccount
        self.name=accName
        print(
            f"\nAccount '{self.name}' created.\nbelance =Rs{self.belance:.2f}"
        )
    def get_belance(self ):
        print(
            f"\nAccount '{self.name}'\nbelance =Rs{self.belance:.2f}"
        )
        
    def Deposit(self, amount):
        self.belance = self.belance+amount
        print("Deposite is completed. ✅")
        self.get_belance()
    def VariableTransication(self , amount):
        if(self.belance>=amount):
            return
        else:
            raise BelanceException(
                f" sorry Account '{self.name}' only has a belance '{self.belance:.2f}"
            )
    def withdraw(self , amount):
        try:
            self.VariableTransication(amount)
            self.belance = self.belance - amount
            print("Withdraw is completed. ✅")
            self.get_belance()
        except BelanceException as error:
            print(f"\nWithdraw is intrrupted: {error}.")
    
    def transfer(self , amount,account):
        try:
            print("\n***************\n\nAmount is transfering... 🔃\n\n")
            self.VariableTransication(amount)
            self.withdraw(amount)
            account.Deposit(amount)
            print("\nTransfered succesfully ✅\n\n***************")
        except BelanceException as error:
            print(f"\nTransfer is intrrupted!❌.{error}")
            

class IntrestRewardsAcct(BankAccount):
    def Deposit(self, amount):
        self.belance=self.belance+(amount*1.05)
        print("\n Deposit completed.✅")
        self.get_belance()



