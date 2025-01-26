class BankAccount:
    def __init__(self, initialAccount, accName):
        self.belance=initialAccount
        self.name=accName
        print(
            f"\nAccount '{self.name}' created.\nbelance =Rs{self.belance:.2f}"
        )
        