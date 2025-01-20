
def naturalNumberSum(num):
    if num==0:
        return 0
    
    return naturalNumberSum(num-1)+num

num=int(input("Enter a antural number : "))
sum=naturalNumberSum(num)
print(sum)