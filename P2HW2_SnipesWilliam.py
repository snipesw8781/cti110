#CTI-110
#P2HW2 - List
#William Snipes
#9/19/2023
#

#Enter grade for Module 1: 65.5
#Enter grade for Module 2: 88
#Enter grade for Module 3: 78.5
#Enter grade for Module 4: 90
#Enter grade for Module 5: 61
#Enter grade for Module 6: 92
#--------------Results--------------
#Lowest Grade:        61.0
#Highest Grade:       92.0
#Sum of Grades:       475.0
#Average:             79.17

mod1 = float(input("Enter grade for Module 1:"))
mod2 = float(input("Enter grade for Module 2:"))
mod3 = float(input("Enter grade for Module 3:"))
mod4 = float(input("Enter grade for Module 4:"))
mod5 = float(input("Enter grade for Module 5:"))
mod6 = float(input("Enter grade for Module 6:"))
grades = [mod1, mod2, mod3, mod4, mod5, mod6]
print("-------------Results-------------")
print(f'Lowest Grade:       {min(grades)}')
print(f'Highest Grade:      {max(grades)}')
print(f'Sum of Grades:      {sum(grades)}')
average = sum(grades)/len(grades)
print("Average:           ",round(average,2))
print("-----------------------------------------")
