num = int(input())
while num>= 10:
    digit_sum = 0
    temp = num
    while temp >0:
        digit_sum += temp%10
        temp  = temp//10
    num = num-digit_sum
print(num)
