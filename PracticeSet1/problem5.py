salary = int(input("Enter the salary: "))
late_days = int(input("your late days: "))
absent_days = int(input("your absent days: "))
final_salary = 0
if late_days > 5:
    final_salary =salary - salary*0.05
elif  late_days > 10:
    final_salary  = salary - salary*0.10
elif absent_days > 2:
    final_salary= salary - salary*0.05

print(final_salary)