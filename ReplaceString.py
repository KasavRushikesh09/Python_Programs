input = input("Enter the your name: \n")

if(input < chr(3)):
    print("Invalid Charector should be more than 3")
    exit()
else:
    string = "Hello <<UserName>>, How are you ?"
    replace  = string.replace("<<UserName>>",input)
    print(replace)

