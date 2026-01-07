from random import random

n = int(input("Enter the number: "))
if n<= 0:
    print("Number should be positive")

else:
    head = 0
    tail = 0

    value = random()
    if value <0.5:
        tail += 1
    else:
        head += 1

    head_per = (head/n)*100
    tail_per = (tail/n)*100

    print(f"head:{head_per:.2f}%")
    print(f"tail:{tail_per:.2f}%")

