def show_Balance():
   print(f"Your balance is ${balance:.2f}")

def deposite():
   amount =float(input("Enter your amount for deposite : "))
   if(amount < 0):
       return 0
   else:
       return amount
   

def withdraw():
    amount =float(input("Enter your amount for withdraw : "))
    if( amount > balance ) :
        print("Insuffecint amount in your account!")
        return 0
    elif( amount < 0 ):
        print("Amount must be greater than 0 !")
        return 0
    else:
        return amount



balance = 0
is_Runing=True

while is_Runing:
    print("******* WELCOME TO THE BANKING SYSTEM *******")
    print("1. Show the balance. ")
    print("2. Deposit here.   ")
    print("3. Withdraw from here. ")
    print("4. Exit the system. ")
    num=int(input("Enter Your choices (1-4) : "))
    if(num==1):
        show_Balance()
    elif(num==2):
       balance += deposite()
    elif(num==3):
       balance -= withdraw()
    elif(num==4):
        is_Runing=False
    else:
        print("Invalide choise")
print("THANKS FOR USING OUR BANKING SYSTEM.")
