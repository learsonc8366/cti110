# Caylee Learson
# 3-18-25
# P3HW1

# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 1: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)

print()
print('-'*10,'Results','-'*10)
print(f'{'Lowest Grade:':<20} {low}')
print(f'{'Highest Grade:':<20} {high}')
print(f'{'Sum of Grades:':<20} {total}')
print(f'{'Average:':<20} {avg:.2f}')

# determine letter grade for average


if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >=60:
    print('Your grade is: D')
elif avg >= 50:
    print('Your grade is: F') # TO DO: finish this






