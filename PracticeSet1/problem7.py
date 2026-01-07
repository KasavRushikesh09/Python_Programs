amount = int(input("Enter a amount: "))
payment_amount = 0
if amount  >= 5000:
    payment_amount =amount - amount*0.20
elif amount >= 3000:
    payment_amount = amount -amount*0.10
elif amount >= 1000:
    payment_amount = amount-amount*0.05
else:
    payment_amount = amount

print(payment_amount)