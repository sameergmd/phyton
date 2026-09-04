# Student Grading Automation

name = input("Enter student name: ")

marks1 = float(input("Enter marks for Subject 1: "))
marks2 = float(input("Enter marks for Subject 2: "))
marks3 = float(input("Enter marks for Subject 3: "))
marks4 = float(input("Enter marks for Subject 4: "))
marks5 = float(input("Enter marks for Subject 5: "))

total = marks1 + marks2 + marks3 + marks4 + marks5
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n========== STUDENT REPORT ==========")
print("Student Name:", name)
print("Total Marks :", total, "/ 500")
print("Percentage  :", percentage, "%")
print("Grade       :", grade)

if grade == "F":
    print("Result      : FAIL")
else:
    print("Result      : PASS")

print("====================================")
