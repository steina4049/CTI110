# Ashley Stein
# 3/4/2025
# P1HW2
# Make code that calculates travel expenses

budget = int(input("Enter budget: "))
destination = input("Enter your travel destination: ")
gas_expense = int(input("How much do you think you will spend on gas?: "))
accommodation_expense = int(input("Approximately, how much will you need for accommodation/hotel?: "))
food_expense = int(input("Last, how much do you need for food?: "))
total_expenses = gas_expense + accommodation_expense + food_expense
remaining_budget = budget - total_expenses

print("-----Travel Expenses-----")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}")
print(f"Fuel: {gas_expense}")
print(f"Accommodation: {accommodation_expense}")
print(f"Food: {food_expense}")
print(f"Remaining balance: {remaining_budget}")
