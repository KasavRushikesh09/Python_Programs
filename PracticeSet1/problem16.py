num = int(input("Enter a number:  "))
lst = list(map(int,input("Enter the minute: ").split()))

capacity = 1000
curr_volume = 0

for i in range(num):
    curr_volume += lst[i]
    if curr_volume > capacity:
        print(i+1)
        break
