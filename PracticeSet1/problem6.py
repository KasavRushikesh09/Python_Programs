# num1 = int(input())
# num2 = int(input())
#
# count = 0
#
# for n in range(num1 ,num2+1):
#     if n<=1:
#         continue
#     is_prime = True
#     for i in range (2, int(n**0.5)+1):
#         if n%i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         count +=1
#
# print(count)

num1 = int(input())
num2 = int(input())

count = 0
for n in range(num1,num2+1):
    if n <=1:
        continue
    is_prime = True
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            is_prime = False
            break
    if is_prime:
        count += 1
print(count)
