# list = list(map(int,input().split()))
list = [3,7,2,9]
def count_function(list):
    count = 0
    n = len(list)
    for i in range(n):
        for j in range(0,n-i-1):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
                count +=1
    return count
answer = count_function(list)
print(answer)