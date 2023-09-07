# Travel Expense program
# 9/5/2023
# CTI-110 P1HW2 - Travel Expense
# William Snipes
#


print('This program calculates and displays travel expenses.\n')
budget = float(input("Enter Budget:"))
print()

destination = input("Enter your travel destination:")
print()

fuel = float(input("How much do you think you will spend on gas? "))
print()

hotel = float(input("Approximately, how much will you need for accomodation/hotel? "))
print()

food =float(input("Last, how Much do you need for food? "))

#Add expenses
expenses = fuel + hotel + food
balance = budget - expenses

print("\n------------Travel Expenses-----------")
print("Location:",destination)
print("Initial Budget:",budget)

print("\nFuel:",fuel)
print("Accomodation:",hotel)
print("Food:",food)

print("\nRemaining Balance:",balance)

print("\ntotal expenses:",expenses)
