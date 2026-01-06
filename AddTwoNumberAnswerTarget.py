num = [1,2,3,4,5,6,8]
target = 9

for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i]+num[j] == target:
            print(i,j)
        else:
            continue