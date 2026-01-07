drain_per_minute = int(input("Enter the drain per minute: "))

minutes=0
battery = 100

while battery > 0:
    battery = battery - drain_per_minute
    minutes += 1
print(minutes)