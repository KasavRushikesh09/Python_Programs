num = input("Enter the number: ")
is_increasing = True
for i in range(len(num)-1):
    if num[i] >= num[i+1]:
        is_increasing = False
        break
if is_increasing:
    print("Yes")
else:
    print("No")
