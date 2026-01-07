balance = int(input())

n = int(input())

for _ in range(n):
    amount = int(input())
    if amount%100 == 0 or balance >= amount:
        print("Success")
        balance -= amount

    else:
        print("Failed")
print(balance)
