from bankingprojectUssin_OOP import *

Ali=BankAccount(1000, "Ali")
Attia=BankAccount(2000,"Attia")

Ali.get_belance()
Attia.get_belance()
Attia.Deposit(900)
Ali.withdraw(10)
Ali.transfer(1000,Attia)