import sys

if len(sys.argv) != 3:
    print("Usage: python student.py <name> <rollno>")
    sys.exit(1)

name = sys.argv[1]
rollno = sys.argv[2]

print("Student Name:", name)
print("Roll Number:", rollno)
