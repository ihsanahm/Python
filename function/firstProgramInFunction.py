
def calculate_avrage( num1 , num2 , num3 ) :
    avrage=(num1+num2+num3)/3
    return avrage

num1=int(input("Enter the number one : "))
num2=int(input("Enter the number two : "))
num3=int(input("Enter the number three : "))
avrage=calculate_avrage(num1 , num2 , num3 )

print(avrage)