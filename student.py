import sys
        # Check if correct number of arguments are given
if len(sys.argv) != 3:
    print("Usage: python student.py <name> <rollno>")
    sys.exit(1)

# sys.argv[0] is always the program name
script_name = sys.argv[0]
name = sys.argv[1]
rollno = sys.argv[2]

print("Script Name:", script_name)
print("Student Name:", name)
print("Roll Number:", rollno)


