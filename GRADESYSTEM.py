# Simple Grading System in Python

marks = float(input("Enter your marks (0-100): "))

if marks >= 90 and marks <= 100:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
elif marks >= 0:
    print("Grade: F")
else:
    print("Invalid marks! Please enter a value between 0 and 100.")