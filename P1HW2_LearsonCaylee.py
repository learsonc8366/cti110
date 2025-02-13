# Caylee Learson
 # 2-13-2025
 # P1HW2
 # create a program that does some basic math on numbers that are entered.

print("This program calculates and displays travel expenses\n")
budget=int(input("Enter Budget: "))
print()
location=str(input("Enter your travel destination: "))
print()
gas=int(input("How much do you think you will spend on gas? "))
print()
lodging=int(input("Approximately, how much will you need on accomodation/hotel? "))
print()
food=int(input("Last, how much do you need for food? "))
print()
print("------------Travel Expenses------------")
print("Location",location)
print("Initial Budget",budget)
print()
print("Fuel",gas)
print("Accomodation",lodging)
print("Food",food)

# calculation
balance=budget-(gas+lodging+food)
print("Remaining Balance",balance)




 
