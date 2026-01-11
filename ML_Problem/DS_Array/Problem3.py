arr = list(map(int,input("Enter the array: ").split()))
key = int(input("Enter the key"))
count = 0
for i in arr:
    if key == i:
        count += 1
print((count))
