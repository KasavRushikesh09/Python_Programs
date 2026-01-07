unit = int(input("Enter the unit:\n"))
bill =0

if unit <= 100:
    bill = unit*3
elif unit <=200:
    bill = 100*3 + (unit-100)*5
else:
    bill = 100*3 + 100*5 + (unit-200)*8

if bill> 300:
    bill = bill+bill*0.10
print(int(bill))