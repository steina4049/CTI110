# Ashley Stein 
# 4/24/2025
# P4HW2
# This program calculates regular pay, overtime pay, and gross pay and summarize totals at the end.

# Initialize overall totals
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

# Step 1: Start sentinel loop
while True:
    name = input("Enter employee's name or 'Done' to terminate: ")

    if name == "Done":
        break  # Exit loop when sentinel is entered

    # Input for hours worked
    while True:
        try:
            hours_worked = float(input(f"Enter number of hours worked for {name}: "))
            break  # If conversion to float succeeds, break the loop
        except ValueError:
            print("Invalid input. Please enter a valid number for hours worked.")

    # Input for pay rate
    while True:
        try:
            pay_rate = float(input(f"Enter {name}'s pay rate: $"))
            break  # If conversion to float succeeds, break the loop
        except ValueError:
            print("Invalid input. Please enter a valid number for pay rate.")

    # Step 2: Initialize pay calculations
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = 0

    # Step 3: Check for overtime
    if hours_worked > 40:
        regular_hours = 40
        regular_pay = regular_hours * pay_rate
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
    else:
        regular_hours = hours_worked
        regular_pay = regular_hours * pay_rate

    # Step 4: Calculate gross pay
    gross_pay = regular_pay + overtime_pay

    # Step 5: Display employee's payroll details
    print("\n----------------------------------------")
    print(f"{'Employee name:':<20}{name}")
    print("\n{:<15}{:<12}{:<10}{:<15}{:<15}{:<10}".format(
        "Hours Worked", "Pay Rate", "OverTime", "OverTime Pay", "RegHour Pay", "Gross Pay"
    ))
    print("--------------------------------------------------------------------------")
    print("{:<15.2f}{:<12.2f}{:<10.2f}${:<14.2f}${:<14.2f}${:<10.2f}".format(
        hours_worked, pay_rate, overtime_hours, overtime_pay, regular_pay, gross_pay
    ))

    # Step 6: Update totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

# Step 7: Display summary
print("\n========================================")
print("Summary of all employees entered:")
print("========================================")
print(f"Total number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
