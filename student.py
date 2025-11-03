import sys

if len(sys.argv) == 3:
    name = sys.argv[1]
    rollno = sys.argv[2]
    print("✅ User provided input values:")
    print("Student Name:", name)
    print("Roll Number:", rollno)
else:
    name = "Deepa"   # Default value
    rollno = "101"   # Default value
    print("⚙️ No input given — using default values:")
    print("Student Name:", name)
    print("Roll Number:", rollno)
