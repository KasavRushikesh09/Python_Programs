remaining_seat = 40
seat = int(input())

for _ in range(seat):
    request = int(input())
    if request <= remaining_seat:
        remaining_seat -= request
        print("Confirmed")
    else:
        print("Waitlisted")