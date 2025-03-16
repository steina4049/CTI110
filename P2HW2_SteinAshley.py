#Ashley Stein
#3/16/2025
#P2HW2
#Create a code that accumlates grades

module_1 = float(input("Enter grade for Module 1: "))
module_2 = float(input("Enter grade for Module 2: "))
module_3 = float(input("Enter grade for Module 3: "))
module_4 = float(input("Enter grade for Module 4: "))
module_5 = float(input("Enter grade for Module 5: "))
module_6 = float(input("Enter grade for Module 6: "))

grades = [module_1, module_2, module_3, module_4, module_5, module_6]

lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)

print("-----Grade Summary-----")
print(f"Lowest grade: {lowest_grade:.2f}")
print(f"Highest grade: {highest_grade:.2f}")
print(f"Sum of grades: {sum_of_grades:.2f}")
print(f"Average grade: {average_grade:.2f}")
