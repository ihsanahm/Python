from bankingprojectUssin_OOP import *

Ali=BankAccount(1000, "Ali")
Attia=BankAccount(2000,"Attia")

Ali.get_belance()
Attia.get_belance()
Attia.Deposit(900)
Ali.withdraw(10)
Ali.transfer(1000,Attia)
Haseeb=IntrestRewardsAcct(1000,"Haseeb")
Haseeb.get_belance()
Haseeb.Deposit(100)
Haseeb.transfer(100,Ali)
Safeer=SavingAcct(1000,"Safeer")
Safeer.get_belance()
Safeer.Deposit(100)
Safeer.transfer(200,Attia)
