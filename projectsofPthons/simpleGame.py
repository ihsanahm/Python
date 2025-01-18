import random

def spin_row():
    symbols = ["🍒", "🔔", "🍉", "🍋", "⭐"]
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("***************")
    print(" | ".join(row))
    print("***************")

def pay_out(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 6
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '🍉':
            return bet * 20
        elif row[0] == '🍋':
            return bet * 30
        elif row[0] == '⭐':
            return bet * 40
    return 0  # Explicitly return 0 for non-matching rows.

def deposit():
    while True:
        try:
            amount = float(input("Enter your amount for deposit: "))
            if amount > 0:
                return amount
            print("Amount must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    balance = 0
    print("***********************************")
    print(" WELCOME TO PYTHON SLOTS ")
    print("***********************************\n")
    print("***********************************")
    print("Symbols: 🍒 🔔 🍉 🍋 ⭐")
    print("***********************************")

    if balance == 0:
        print("Please deposit your amount to play the game.")
        balance += deposit()
        if balance > 0:
            while balance > 0:
                print(f"Your current balance is: ${balance}")
                bet = input("Enter your bet amount: ")
                if not bet.isdigit():
                    print("Please enter a valid number!")
                    continue
                bet = int(bet)

                if bet > balance:
                    print("Insufficient balance in your account.")
                    continue
                if bet <= 0:
                    print("Bet must be greater than 0.")
                    continue

                balance -= bet
                row = spin_row()
                print("Spinning...\n")
                print_row(row)
                payout = pay_out(row, bet)
                if payout > 0:
                    print(f"You won ${payout}!")
                else:
                    print("Sorry, you lost this round. ☹️☹️☹️")
                balance += payout
                
                pay_again=input("Do you want spain again? (Y/N) : ")
                if pay_again != 'Y':
                    break
            print("*********************************************")
            print(f"Game over! your final score is : ${balance}")
            print("*********************************************")
        else:
            print("Sorry, you have insufficient funds in your account!")
    else:
        pass

main()
