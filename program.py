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

# Check even/odd
if total % 2 == 0:
    print(f"The sum ({total}) is Even")
else:
    print(f"The sum ({total}) is Odd")
