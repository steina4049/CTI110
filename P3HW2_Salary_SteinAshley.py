# Ashley Stein  

# 4/7/2025

# P3HW2

# This program calculates an employee's gross pay, including regular and overtime hours, and displays results.


# Pseudocode:
# 1. Start program
# 2. Ask for the name of the employee
# 3. Ask for the number of hours the employee worked this week
# 4. Ask for the pay rate of the employee
# 5. If the number of hours worked is more than 40 (overtime):
#    a. Calculate regular pay for the first 40 hours
#    b. Calculate overtime pay for any hours over 40 (overtime pay rate = 1.5 * regular rate)
# 6. If the number of hours worked is 40 or less:
#    a. Calculate the pay for regular hours only
# 7. Calculate the total gross pay (regular pay + overtime pay)
# 8. Display the employee's name, pay rate, hours worked, overtime hours, overtime pay, regular pay, and gross pay 
# 9. End program

def main():
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
    print("\n-------------------------------")
    print(f"{'Employee name:':<20}{name}")
    print("\nHours worked    Pay Rate    Overtime   OverTime Pay     RegHour Pay       Gross Pay")
    print("----------------------------------------------------------------------------------------")
    print(f"{hours_worked:<15} {pay_rate:<12.2f} {overtime_hours:<10.2f} {overtime_pay:<15.2f} ${regular_pay:<15.2f} ${gross_pay:<10.2f}")

main ()
