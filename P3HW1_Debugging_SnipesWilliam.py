#CTI-110
#P3HW1 - Debugging
#William Snipes
#10/3/2023

#Enter grade for Module 1: 86.5
#Enter grade for Module 2: 80
#Enter grade for Module 3: 76.9
#Enter grade for Module 4: 90
#Enter grade for Module 5: 79
#Enter grade for Module 6: 88
#--------------Results--------------
#Lowest Grade:        76.9
#Highest Grade:       90.0
#Sum of Grades:       500.4
#Average:             83.40
#--------------------------------------------
#Your grade is: B
# This program takes a number grade , determines average and displays letter grade for average.
# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5]

# TO DO: determine lowest, highest , sum and average for grades

print("-------------Results-------------")
print(f'Lowest Grade:       {min(grades)}')
print(f'Highest Grade:      {max(grades)}')
print(f'Sum of Grades:      {sum(grades)}')
average = sum(grades)/len(grades)
print("Average:           ",round(average,2))
print("-----------------------------------------")

# determine letter grade for average

if average >= 90:
    print('Your grade is: A')
elif average >= 80:
    print('Your grade is: B')
elif average >= 70:
    print('Your grade is: C')
elif average >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')  # TO DO: finish this









