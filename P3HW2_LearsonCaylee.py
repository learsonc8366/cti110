name = input("Enter employees name: ")
hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter employee's pay rate: "))

if hours > 40:
    reg_pay = 40 * rate
    ovt_hrs = hours - 40
    ovt_pay = ovt_hrs * rate * 1.5
    gross_pay = ovt_pay + reg_pay
else:
    reg_pay = hours * rate
    ovt_hrs = 0
    ovt_pay = 0
    gross_pay = 0

print(gross_pay)
print(reg_pay)