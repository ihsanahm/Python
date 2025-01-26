class BelanceException():
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
            f"\nAccount '{self.name}' created.\nbelance =Rs{self.belance:.2f}"
        )
        
    def Deposite(self, ammount):
        self.belance = self.belance+ammount
        print("Deposite is completed.")
    def VariableTransication(self , ammoun):
        if(ammoun>=self.belance):
            return
        else:
            raise BelanceException(
                f" sorry Account '{self.name}' only has a belance '{self.belance:.2f}"
            )
