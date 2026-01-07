distance = int(input("Enter the number: "))
age = int(input("Enter the age: "))
rupees = 0
dist =distance*2
if age >=60:
    rupees = dist - (dist*0.30)
elif age < 12:
    rupees  = dist - (dist*0.50)
print("Rupees: ", rupees)

    