print(" <<==== *** Welcome to our login system *** ====>>")
name = input("Enter your Name : ")
# password = input("Enter your password : ")
# tuple is use to save a user name and password 
tup=("Ihsan",)
tup2=("Narejo",)
#  first check the user name 
if name in tup:
    index=tup.index(name)
    password = input("Enter your password: ")
    # Validate password
    if password == tup2[index]:
        print("Your login was successful!")
    else:
        print("Invalid password!")
else:
    print("Invalid UserName!")



