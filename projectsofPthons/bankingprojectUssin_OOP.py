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
        