# CTI-110
# P4HW2 - Salary Calcutor 
# Wlliam Snipes
# 11/2/23
#

#Enter employee's name or "Done" to terminate: Nancey Drew
#How many hours did Nancey Drew hours work: 39
#What is Nancey Drew's pay rate?: 20
#-----------------------------
#Enter employee's name: Nancey Drew
#
#Hours Worked   Pay Rate    OverTime       OverTme Pay    RegHour Pay    Gross Pay
#---------------------------------------------------------------------------------
#39.0           20.0        0.0            0.0         $780.00        $780.00
#
#
#Enter employee's name or "Done" to terminate: Ricky Hardy
#How many hours did Ricky Hardy hours work: 45
#What is Ricky Hardy's pay rate?: 18.5
#-----------------------------
#Enter employee's name: Nancey Drew
#
#Hours Worked   Pay Rate    OverTime       OverTme Pay    RegHour Pay    Gross Pay
#---------------------------------------------------------------------------------
#45.0           18.50       5.0            138.75         $740.00        $878.75
#
#
#Enter employee's name or "Done" to terminate: Done
#
#Total number of employees entered: 2
#Total amount paid for overtime: $138.75
#Total amount paid for Regular hours: $1520.00
#Total amount paid in gross: $1658.75

def calculate_gross_pay(hours_worked, pay_rate):
    regular_hours = min(hours_worked, 40)
    overtime_hours = max(hours_worked - 40, 0)

    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * 1.5 * pay_rate

    gross_pay = regular_pay + overtime_pay

    return regular_hours, overtime_hours, regular_pay, overtime_pay, gross_pay

def main():
    total_overtime_pay = 0
    total_regular_pay = 0
    total_gross_pay = 0
    total_employees = 0

    while True:
        employee_name = input("Enter employee's name or 'Done' to terminate: ")
        if employee_name.lower() == 'done':
            break

        hours_worked = float(input(f"How many hours did {employee_name} work? "))
        pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

        regular_hours, overtime_hours, regular_pay, overtime_pay, gross_pay = calculate_gross_pay(hours_worked, pay_rate)

        total_overtime_pay += overtime_pay
        total_regular_pay += regular_pay
        total_gross_pay += gross_pay
        total_employees += 1

        print("\n----------------------------")
        print(f"Enter employee's name: {employee_name}\n")
        print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<20}{"Regular Pay":<14}{"Gross Pay"}')
        print("-------------------------------------------------------------------------------------")
        print(f"{hours_worked:<15.1f}{pay_rate:<12.2f}{overtime_hours:<12.1f}{overtime_pay:<20.2f}${regular_pay:<14.2f}${gross_pay:<.2f}\n")

    print(f"\nTotal number of employees entered: {total_employees}")
    print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
    print(f"Total amount paid for Regular hours: ${total_regular_pay:.2f}")
    print(f"Total amount paid in gross: ${total_gross_pay:.2f}")

    restart = input("Do you want to enter more employees? (yes/no): ")
    if restart.lower() != 'yes':
            print("Have a great day!")
            return

if __name__ == "__main__":
    main()

