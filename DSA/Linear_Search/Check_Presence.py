lst = list(map(int,input("Enter the numbers: ").split()))
numbers = int(input("Enter the key:"))

def check_presence(lst,numbers):
    for i in range(len(lst)):
        if lst[i] == numbers:
            return i
    return -1

result = check_presence(lst,numbers)
if result != -1:
    print("Yes")
else:
    print("No")
