number = [10,20,60,40,79,50,20,30,20,70]
target = 20

def Last_Occurence(arr,key):
    count = -1
    for i in range(len(arr)):
        if(arr[i] == key):
            count = i
    return count

result = Last_Occurence(number,target)
print(result)