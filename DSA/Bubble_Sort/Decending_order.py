# list = list(map(int,input("Enter :").split()))
list = [3,7,2,9]
def descending_order(list):
    n = len(list)
    for i in range(n):
        for j in range(0,n-i-1):
            if list[j] < list[j+1]:
                list[j],list[j+1]  = list[j+1],list[j]

    return list

result = descending_order(list)
print(result)