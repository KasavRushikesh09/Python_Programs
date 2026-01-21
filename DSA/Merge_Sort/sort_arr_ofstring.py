list = ["mango","apple","banana"]

def merge_sort(list):
    if len(list) <= 1:
        return list
    n = len(list)
    mid = len(list) //2

    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])

    return merge(left,right)
def merge(left,right):
    i = j = 0
    result = []
    while i<len(left) and j <len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result += left[i:]
    result += right[j:]
    return result
print(merge_sort(list))


