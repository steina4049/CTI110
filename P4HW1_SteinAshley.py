#Ashley Stein
#4/24/2025
#P4HW1
#Enter scores for grading and evaluation


# Ask how many scores the user wants to enter
num_scores = int(input("How many scores would you like to enter? "))

# Initialize the list to store scores
valid_scores = []

# Collect valid scores
for i in range(num_scores):
    while True:
        try:
            score = float(input(f"Enter score #{i+1}: "))
            if 0 <= score <= 100:
                valid_scores.append(score)
                break  # Exit the loop if score is valid
            else:
                print("INVALID Score entered!!!!")
                print("Score should be between 0 and 100")
        except ValueError:
            print("Invalid input.")

# Find the lowest score
lowest_score = min(valid_scores)

# Remove the lowest score and make a new list
modified_scores = valid_scores.copy()
modified_scores.remove(lowest_score)

# Calculate the average of modified list
average_score = sum(modified_scores) / len(modified_scores)

# Determine letter grade
if average_score >= 90:
    grade = 'A'
elif average_score >= 80:
    grade = 'B'
elif average_score >= 70:
    grade = 'C'
elif average_score >= 60:
    grade = 'D'
else:
    grade = 'F'

# Display results
print("\n-------Results-------:")
print(f"Lowest Score  : {lowest_score}")
print(f"Modified List : {modified_scores}")
print(f"Scores Average: {average_score:.2f}")
print(f"Grade         : {grade}")
print("------------------------")
