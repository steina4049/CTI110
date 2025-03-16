# Ashley Stein
# 3/16/2025
# P2HW1
# Change how results are displayed.

budget = float(input("Enter budget: "))
destination = input("Enter your travel destination: ")
gas_expense = float(input("How much do you think you will spend on gas?: "))
accommodation_expense = float(input("Approximately, how much will you need for accommodation/hotel?: "))
food_expense = float(input("Last, how much do you need for food?: "))
total_expenses = gas_expense + accommodation_expense + food_expense
remaining_budget = budget - total_expenses

print("-----Travel Expenses-----")
print(f"Location: {destination}")
print(f"Initial Budget: ${budget:,.2f}")
print(f"Fuel: ${gas_expense:,.2f}")
print(f"Accommodation: ${accommodation_expense:,.2f}")
print(f"Food: ${food_expense:,.2f}")
print(f"Remaining balance: ${remaining_budget:,.2f}")
