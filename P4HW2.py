name = input("Enter employee's name or \"Done\" to terminate: ")

overTime_total = 0.0
regPay_total = 0.0
gross_total = 0.0
Employee_count = 0
while name !="Done":
    Employee_count +=1
    hoursWorked = float(input("How many hours did "+name+" work? "))
    payRate = float(input("What is "+name+"'s pay rate? "))
    if hoursWorked >40 :
        print("regular pay")

    else:
        print("over time pay")
    
    print("\nEmployee name: ",name,"\n")
    print(f'{"Hours worked":<15}{"Pay rate":<12}{"Overtime":<12}{"Overtime Pay":<20}{"RegHour Pay":<20}{"Gross Pay:"}')
    print('-----------------------------------------------------------------------------------------')
    print()

    name = input("Enter employee's name or \"Done\" to terminate: ")


print("\nTotal number of employees entered: ", Employee_count, sep="")
print("Total amount paid for overtime: $", format(overTime_total,".2f"), sep="")
print("Total amount paid for regular hours: $", format(regPay_total,".2f"), sep="")
print("Total amount paid in gross: $", format(gross_total,".2f"), sep="")