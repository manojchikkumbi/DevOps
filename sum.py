import sys

# Check if two numbers are provided
if len(sys.argv) != 3:
    print("Usage: python program.py <num1> <num2>")
    sys.exit()
else:
    print("Arguments received successfully!")

# Convert arguments to integers
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

# Find sum
total = num1 + num2

# Print script name (optional)
script_name = sys.argv[0]
num1=15
num2=20
print(f"Script name: {script_name}")

# Check even/odd
if total % 2 == 0:
    print(f"The sum ({total}) is Even")
else:
    print(f"The sum ({total}) is Odd")
