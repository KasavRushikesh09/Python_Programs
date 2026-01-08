num = int(input())

original = num
reversed = 0

while num >0:
    digit = num%10
    reversed = reversed*10+digit
    num = num//10
if reversed == original:
    print("Palindrome")
else:
    print("Not Palindrome")