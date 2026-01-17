lst = list(map(int,input("Enter the number: ").split()))
key = int(input("Enter the key: "))

def count_occurence(lst,key):
    count = 0
    for i in range(len(lst)):
        if lst[i] == key:
            count += 1
    return count

result = count_occurence(lst,key)

print(result)