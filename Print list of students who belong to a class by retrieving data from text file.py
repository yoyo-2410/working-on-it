# Program: Print list of students who belong to a class by retrieving data from text file

# Example file format (students.txt):
# Name,Class
# Rahul,10
# Priya,9
# Arjun,10
# Meena,8

filename = "students.txt"

cls = input("Enter class to search: ")

try:
    with open(filename, "r") as f:
        print(f"\nStudents in class {cls}:")
        found = False
        for line in f:
            name, student_class = line.strip().split(",")
            if student_class == cls:
                print(name)
                found = True
        if not found:
            print("No students found for this class.")
except FileNotFoundError:
    print("File not found! Please ensure 'students.txt' exists.")
