arr = [4,1,2,7,3]

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_value = i
        for j in range(i+1,n):
            if arr[j] < arr[min_value]:
                min_value = j
        print(arr[min_value], end=" ")
        arr[i],arr[min_value] = arr[min_value],arr[i]
selection_sort(arr)