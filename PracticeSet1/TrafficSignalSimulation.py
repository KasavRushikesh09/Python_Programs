T = int(input("Enter the time:"))

t = T%90

if t == 0:
    t == 90
if 1 <= t <= 30:
    print("Red")
elif 31 <= t <= 45:
    print("Green")
elif 45 <= t <= 60:
    print("yellow")