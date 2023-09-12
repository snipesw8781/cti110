# Travel Expense program
# 9/12/2023
# CTI-110 P2HW1 - Travel 
# William Snipes
#


print('This program calculates and displays travel expenses.\n')
budget = float(input("Enter Budget:"))
print()

destination = input("Enter your travel destination:")
print()

fuel = float(input("How much do you think you will spend on gas? "))
print()

hotel = float(input("Approximately, how much will you need for accommodation/hotel?"))
print()

food = float(input("Last, how Much do you need for food? "))

# Add expenses
expenses = fuel + hotel + food
balance = budget - expenses

print("------------Travel Expenses-----------")
print("Location:          {}".format(destination))
print("Initial Budget:    ${:,.1f}".format(budget))
print("Fuel:              ${:,.1f}".format(fuel))
print("Accommodation:     ${:,.1f}".format(hotel))
print("Food:              ${:,.1f}".format(food))
print("--------------------------------------")
print("\nRemaining Balance: ${:,.1f}".format(balance))
