import sys

# Check if enough arguments are passed
# sys.argv[0] = script name
if len(sys.argv) == 3:
    name = sys.argv[1]
    rollno = sys.argv[2]
else:
    # Default values (used when no arguments passed)
    name = "Deepa"
    rollno = "101"

print("=== Student Details ===")
print("Student Name:", name)
print("Roll Number:", rollno)



