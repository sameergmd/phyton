with open("log.txt", "w") as file:
    file.write("System started\n")
    file.write("User logged in\n")
    file.write("System closed\n")

with open("log.txt", "r") as file:
    print(file.read())
