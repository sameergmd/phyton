attendance = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    status = input("Enter Present or Absent: ")
    attendance[name] = status

print("\nAttendance Report:")

for name, status in attendance.items():
    print(name, ":", status)
