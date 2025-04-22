# Ashley Stein 
# 4/7/2025
# P3HW2
# This program calculates an employee's gross pay, including regular and overtime hours, and displays results.

# Step 1: Ask user for employee's details
name = input("Enter employee's name: ")

hours_worked = float(input("Enter number of hours worked: "))

pay_rate = float(input("Enter employee's pay rate: $"))

# Step 2: Initialize overtime pay and regular pay variables
overtime_hours = 0
overtime_pay = 0
regular_pay = 0

# Step 3: Check if overtime hours are worked
if hours_worked > 40:
    # Regular pay for the first 40 hours
    regular_hours = 40
    regular_pay = regular_hours * pay_rate

    # Overtime pay for hours above 40
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)

else:
    # No overtime, all hours are regular hours
    regular_hours = hours_worked
    regular_pay = regular_hours * pay_rate

# Step 4: Calculate total gross pay
gross_pay = regular_pay + overtime_pay

# Step 5: Display the results in a formatted manner
print("\n----------------------------------------")
print(f"{'Employee name:':<20}{name}")
print("\n{:<15}{:<12}{:<10}{:<15}{:<15}{:<10}".format(
    "Hours Worked", "Pay Rate", "OT Hours", "OT Pay", "Reg Pay", "Gross Pay"
))
print("--------------------------------------------------------------------------")
print("{:<15.2f}{:<12.2f}{:<10.2f}${:<14.2f}${:<14.2f}${:<10.2f}".format(
    hours_worked, pay_rate, overtime_hours, overtime_pay, regular_pay, gross_pay
))
