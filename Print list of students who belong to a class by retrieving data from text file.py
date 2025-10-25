# Program: Print list of students who belong to a class by retrieving data from text file

# Example file format (students.txt):
# Name,Class
# Rahul,10
# Priya,9
# Arjun,10
# Meena,8

fname = "students.txt"
cls = input("Enter class: ")

try:
    with open(fname) as f:
        studs = [n for n, c in (line.strip().split(",") for line in f) if c == cls]
    print(f"\nStudents in class {cls}:\n" + "\n".join(studs) if studs else "No students found.")
except FileNotFoundError:
    print("File not found! Create 'students.txt' first.")
