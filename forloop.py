# get number of values to sum

num_count = int(input("Enter the number of values to add: "))

# initialize the total accumulator
total = 0

# for loop to get the numbers to add up

for i in range(num_count):
    num = float(input("Enter a number: "))
    total = num + total
print("Total: ", total)