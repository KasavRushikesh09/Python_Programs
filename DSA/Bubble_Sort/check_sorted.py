# list = [7,2,3,4]
#
# def sorted_func(list):
#     n = len(list)
#     for i in range(n):
#         for j in (0,n-i-1):
#             if list[j] > list[j+1]:
#                 list[j],list[j+1] = list[j+1],list[j]
#     return list
# res = sorted_func(list)
# print(res)
arr = [1,9,3,4,5,6]

def bubble_sort(arr):
    n = len(arr)
    swap = False
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                swap = True
                break
    if not swap:
        return "Already Sorted"
    else:
        return "Not Sorted"
print(bubble_sort(arr))