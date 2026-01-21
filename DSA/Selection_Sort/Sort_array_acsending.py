list = [1,5,3,9,7,6,4]

def selection_sort(list):
    n = len(list)
    for i in range(n):
        min_value = i
        for j in range(i+1,n):
            if list[j] < list[min_value]:
                min_value = j
        list[i],list[min_value] = list[min_value],list[i]
    return list

result = selection_sort(list)
print(result)