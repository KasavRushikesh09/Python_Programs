arr = list(map(int,input("Enter  the element: ").split()))

key = int(input("Enter the key: "))

if key in arr:
    arr.remove(key)
print(list(arr))

