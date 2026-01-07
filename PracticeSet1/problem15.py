pin = input("Enter pin number: ")
access_attempt = False

for _ in range(3):
    attempt = input("Enter attempt: ")
    if attempt == pin:
        access_attempt = True
        break
if access_attempt:
    print("Access Granted")
else:
    print("Access Denied")