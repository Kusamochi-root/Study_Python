# score.py

# Ask the user for their score and convert it to an integer
score_input = input("Enter your score (0-100): ")
score = int(score_input)

# Check the score using if-elif-else logic
if score >= 90:
    print("Grade: A - Excellent work!")
elif score >= 80:
    print("Grade: B - Very good.")
elif score >= 70:
    print("Grade: C - You passed.")
elif score >= 60:
    print("Grade: D - You might want to study more.")
else:
    print("Grade: F - Failed. Better luck next time!")