 #Caylee Learson
#3-4-25
#P2WH2
#Write program Pseudocode (detail algorithm) and add it as a comment block.

module1 = float(input("Enter grade for Module 1. "))
module2 = float(input("Enter grade for Module 2. "))
module3 = float(input("Enter grade for Module 3. "))
module4 = float(input("Enter grade for Module 4. "))
module5 = float(input("Enter grade for Module 5. "))
module6 = float(input("Enter grade for Module 6. "))
gradeList = [] # empty list
gradeList =[module1, module2, module3, module4, module5, module6] # add variables to the list

# figure out the lowest, highest, sum and the length

lowest = min(gradeList)
highest = max(gradeList)
total = sum(gradeList)
average = total / len(gradeList)

# print the results
print("\n----------Results----------")
print(f'{"Lowest Grade: ":<20}{lowest}')
print(f'{"Highest Grade: ":<20}{highest}')
print(f'{"Sum of Grades: ":<20}{total}')
print(f'{"Average Grade: ":<20}{average:.2f}')
print('-'*30)