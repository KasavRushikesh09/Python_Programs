arr = [4, 2, 8, 1]

def quick_sort(arr):
    if len(arr)<= 1:
        return arr

    pivot = arr[-1]
    left= []
    right=[]

    for x in arr[:-1]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    return quick_sort(right) + [pivot] + quick_sort(left)

print(quick_sort(arr))