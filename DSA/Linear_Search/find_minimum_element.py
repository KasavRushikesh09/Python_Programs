list = [10,30,50,30,20,70,5,8]

def find_minimum_element(list):
    min = list[0]
    for i in range(1,len(list)):
        if list[i] < min:
            min = list[i]
    return min
print(find_minimum_element(list))
