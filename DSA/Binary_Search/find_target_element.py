list = list(map(int,input("Enter the element:").split()))
target = int(input("Enter the target:"))

def find_target_element(list, target):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low+high) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            low = mid+1
        else:
            high = mid-1

    return -1
result = find_target_element(list,target)
print(result)
