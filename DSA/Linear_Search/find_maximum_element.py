list = [10,30,80,6,40]

def find_maximum_element(list):
    max = list[0]
    for i in range(1,len(list)):
        if list[i] > max:
            max = list[i]
    return max

print(find_maximum_element(list))
