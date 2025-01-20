def printList(list, index):
    if index==len(list):
        return
    print(list[index])
    
    return printList(list,index+1)

list=[1,2,3,4,5,6,7]
printList(list,0)

