def converter( usd ) :
    rupe=270
    total=rupe*usd
    return total


print ( " <--- Welcom to currency converter plateform ---> " )
usd = int ( input (" Enter USD amount : " ) )
rupe = converter ( usd )

print ( " Your total amount in pakistani rupes is : $" , usd , " = " , rupe ) 

