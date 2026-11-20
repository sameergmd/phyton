import json

student = {
    "name": "Sameer",
    "age": 20,
    "marks": 90
}

with open("student.json", "w") as file:
    json.dump(student, file)

with open("student.json", "r") as file:
    data = json.load(file)

print("Student Details:")
print(data)
