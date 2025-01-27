class BelanceException(Exception):
    pass




class BankAccount:
    def __init__(self, initialAccount, accName):
        self.belance=initialAccount
        self.name=accName
        # print(
        #     f"\nAccount '{self.name}' created.\nbelance =Rs{self.belance:.2f}"
        # )
    def get_belance(self ):
        print(
            f"\nAccount '{self.name}' created.\nbelance =Rs{self.belance:.2f}"
        )
        
    def Deposite(self, ammount):
        self.belance = self.belance+ammount
        print("Deposite is completed.")
        self.get_belance()
    def VariableTransication(self , ammoun):
        if(self.belance>=ammoun):
            return
        else:
            raise BelanceException(
                f" sorry Account '{self.name}' only has a belance '{self.belance:.2f}"
            )
    def withdraw(self , amount):
        try:
            self.VariableTransication(amount)
            self.belance = self.belance - amount
            print("Withdraw is completed.")
            self.get_belance()
        except BelanceException as error:
            print(f"\nWithdraw is intrrupted: {error}.")


