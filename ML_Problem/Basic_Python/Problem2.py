data  = "2,3,4,5,7,8,0"

result= list(map(int,data.split(',')))
print("List: " , result)

result1 = tuple(map(int,data.split(',')))
print("Tuple: ",result1)