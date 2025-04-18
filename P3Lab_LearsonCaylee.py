# Caylee Learson
# 3-6-25
# P3Lab
# Calculate change

# get float from the user
change = float(input("Enter an amount of money as a float: "))
# convert the float to an integer
change = int(change * 100)
print(change)

if change == 0:
    print("No Change Due!")

# calculate change for each coin type
# integer division //
num_dollars = change // 100
change = change - (num_dollars * 100)

num_quarters = change // 25
change = change - (num_quarters * 25)

num_dimes = change // 10
change = change - (num_dimes * 10)

num_nickels = change // 5
change = change - (num_nickels * 5)

num_pennies = change // 1
change = change - (num_pennies * 1)

# display amounts used

if num_dollars > 0:
    print(num_dollars, end=' ')
    if num_dollars == 1:
        print("Dollar")
    else:
        print("Dollars")

if num_quarters > 0:
    print(num_quarters, end=' ')
    if num_quarters == 1:
        print("Quarter")
    else:
        print("Quarters")

if num_dimes > 0:
    print(num_dimes, end=' ')
    if num_dimes == 1:
        print("Dime")
    else:
        print("Dimes")

if num_nickels > 0:
    print(num_nickels, end=' ')
    if num_nickels == 1:
        print("Nickel")
    else:
        print("Nickels")

if num_pennies > 0:
    print(num_pennies, end=' ')
    if num_pennies == 1:
        print("Penny")
    else:
        print("Pennies")