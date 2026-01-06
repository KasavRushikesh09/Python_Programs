lst = list(map(int, input("Enter the number: ").split()))

for num in range(len(lst)):
     for num2 in range(num+1,len(lst)):
         if lst[num] == lst[num2]:
             print(lst[num])
             break

