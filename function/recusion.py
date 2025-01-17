def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
n = int ( input (" Enter a number : " ) )
show(n)