with open("students.txt", "w") as file:
    n = int(input("Enter number of students: "))

    for i in range(n):
        name = input("Enter student name: ")
        marks = input("Enter marks: ")
        file.write(name + " " + marks + "\n")

with open("students.txt", "r") as file:
    print("\nStudent Records:")
    print(file.read())
