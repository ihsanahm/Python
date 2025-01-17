tup=(22,11,4,5,7,8,0,222,111,33,)

num=int(input("Enter the Number for checking in tuple : "))

i=0

while i<len(tup):
    if(tup[i]==num):
        print(num,"Number is found at Index ",i)
        break    
    i+=1

