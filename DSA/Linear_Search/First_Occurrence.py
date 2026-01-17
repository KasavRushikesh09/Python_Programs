lst  = [10,30,40,60,40,90,40]
key = 40

def first_occurence(lst,key):
    count = 0
    for i in range(len(lst)):
        if lst[i] == key:
            count +=1
            if count == 2 :
                return i
    return -1

result = first_occurence(lst,key)
print(result)
