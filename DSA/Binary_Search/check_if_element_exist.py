list = [10,20,30,40,50,60,70]
target = 10

def check_if_element_exist(list,target):
    low = 0
    high = len(list)-1
    while low <= high:
        mid =(low+high)//2
        if list[mid] == target:
            return True
        elif list[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return False

print(check_if_element_exist(list,target))