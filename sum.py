import sys

# Default values
num1 = 15
num2 = 20

# If user provides two arguments, use them instead of defaults
if len(sys.argv) == 3:
    print("Arguments received successfully!")
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
else:
    print("No arguments provided — using default values (15 and 20).")

# Find sum
total = num1 + num2

# Print script name
script_name = sys.argv[0]

# Check even/odd
if total % 2 == 0:
    print(f"The s
