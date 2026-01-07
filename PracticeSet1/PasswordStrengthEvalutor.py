password = input("Enter the password: ")

isDigit = False
isUpper = False

if len(password) >= 8:
    for ch in password:
        if ch.isdigit():
            isDigit = True
        elif ch.isupper():
            isUpper = True

if len(password) >=8 and isDigit and isUpper:
    print("Strong password")
else:
    print("Weak password")