import sys

# Default values
num1 = 155
num2 = 200

# Try to get command-line arguments
try:
    if len(sys.argv) > 1 and sys.argv[1].strip() != "":
        num1 = int(sys.argv[1])
    if len(sys.argv) > 2 and sys.argv[2].strip() != "":
        num2 = int(sys.argv[2])
except ValueError:
    print("Invalid input! Using default values (15 and 20).")

# Find sum
total = num1 + num2

# Check even/odd
if total % 2 == 0:
    print(f"The sum ({total}) is Even")
else:
    print(f"The sum ({total}) is Odd")

# Get script name
script_name = sys.argv[0]
print(f"Script name: {script_name}")
