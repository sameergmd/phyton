import csv

with open("payroll.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Salary"])

    n = int(input("Enter number of employees: "))

    for i in range(n):
        name = input("Enter employee name: ")
        salary = int(input("Enter salary: "))
        writer.writerow([name, salary])

with open("payroll.csv", "r") as file:
    reader = csv.reader(file)

    print("\nPayroll Details:")

    for row in reader:
        print(row)
