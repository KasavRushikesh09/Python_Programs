list = [4,1,7,3]

def selection_sort(list):
    n = len(list)
    for i in range(n):
        min_value = i
        for j in range(i+1,n):
            if list[j] > list[min_value]:
                min_value = j
        list[i],list[min_value] = list[min_value],list[i]
    return list

result = (selection_sort(list))
print(result)