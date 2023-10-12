# CTI-110
# P3HW2 - Salary
# Wlliam Snipes
# 10/5/23
#

#Enter employee's name: John Smith
#Enter number of hours worked: 45
#Enter emploee's pay rate: 17.5
#-----------------------------
#Enter employee's name: John Smith
#
#Hours Worked   Pay Rate    OverTime       OverTme Pay    RegHour Pay    Gross Pay
#---------------------------------------------------------------------------------
#45.0           17.5        5.0            131.25         $700.00        $831.25


def calculate_gross_pay(hours_worked, pay_rate):
    regular_hours = min(hours_worked, 40)
    overtime_hours = max(hours_worked - 40, 0)
    
    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * 1.5 * pay_rate
    
    gross_pay = regular_pay + overtime_pay
    
    return regular_hours, overtime_hours, regular_pay, overtime_pay, gross_pay

def main():
    employee_name = input("Enter employee's name: ")
    hours_worked = float(input("Enter number of hours worked: "))
    pay_rate = float(input("Enter employee's pay rate: "))
    
    regular_hours, overtime_hours, regular_pay, overtime_pay, gross_pay = calculate_gross_pay(hours_worked, pay_rate)
    
    print("\n----------------------------")
    print(f"Enter employee's name: {employee_name}\n")
    print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<20}{"Regular Pay":<14}{"Gross Pay"}')
    print("-------------------------------------------------------------------------------------")
    print(f"{hours_worked:<15.1f}{pay_rate:<12.2f}{overtime_hours:<12.1f}{overtime_pay:<20.2f}${regular_pay:<14.2f}${gross_pay:<.2f}")

if __name__ == "__main__":
    main()
