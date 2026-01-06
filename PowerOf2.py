x = int(input("Enter a base:"))
n = int(input("Enter a number: "))

result = 1

if 0<=n<=31:
    for i in range(n):
        result = result*x
    print(result)
else:
    print("Invalid Input")