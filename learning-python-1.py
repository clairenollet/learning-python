# Create a file with w mode

file = open("hello.txt", "w")
file.write("Hello, world!")
file.close()

# Read a file with default r mode

with open("hello.txt") as file:
    for line in file:
     print(line)