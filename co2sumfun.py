print("SUM OF ALL ITEMS IN A LIST USING FUNCTION:\n")
def sumlist(list1):
    total=0
    for i in list1:
        total+=i
    return total

list1=[1,2,3,4,5]
result=sumlist(list1)
print("Sum of the list: ",result)
