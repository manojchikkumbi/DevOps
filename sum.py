import sys

# If user provides two arguments, use them instead of defaults
if len(sys.argv) == 3:
    print("Arguments received successfully!")
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
else:
    print("No arguments provided — using default values (15 and 20).")
    # Default values
    num1 = 300
    num2 = 500

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
