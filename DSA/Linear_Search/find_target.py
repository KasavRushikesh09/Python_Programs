numbers = list(map(int,input("Enter the value: ").split()))
target = int(input("Enter the target: "))

def linear_search(arr , key):
    for i in range(len(arr)):
        if(arr[i] == key):
            return i
    return -1

answer = linear_search(numbers, target)
if answer != -1:
    print("Target index numbers is: ",answer)
else:
    print("Target in not found.")