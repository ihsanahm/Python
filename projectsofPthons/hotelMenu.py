# create a hotel menu using dictionary data structures 

menu={
    "Pizza":200,
    "Burger":100,
    "Sandwich":350,
    "pasta":120,
    "coffee":80,
    "Cool Drinks":90
}

print("<<<===**** Welcome to our restaurant ****===>>>")
print("This is our menu selecte your favrouate food :)")
print("Pizza 🍕🍕 : Rs200\nBurger 🍔🍔 : Rs100\nSandwich 🥪🥪 : Rs350\npasta 🍝🍝 : 120\ncoffee 🍵🍵 : Rs80\nCool Drinks 🍷🍷 : Rs90")

total=0
is_true=True

while is_true:
    item=input("Enter the name of the item you want to order :")
    if item in menu:
        total +=menu[item]
    else:
        print(" This item is not available")
    item1=input("Do you want more item (Y/N) : ")
    if item1=='Y':
        is_true=True
    else:
        is_true=False
print(f"Your total bill is Rs{total}.")


