import sys

# Function to get numbers from user input
def get_numbers_from_input():
    while True:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input! Please enter integers only.\n")

# Check if two command-line arguments are provided
if len(sys.argv) == 3:
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        print("Arguments received successfully!")
    except ValueError:
        print("Error: Command-line arguments must be integers.")
        num1, num2 = get_numbers_from_input()
else:
    print("No valid command-line arguments provided — using interactive input.")
    num1, num2 = get_numbers_from_input()

# Calculate the sum
total = num1 + num2

# Check even/odd
if total % 2 == 0:
    print(f"The sum ({total}) is Even")
else:
    print(f"The sum ({total}) is Odd")

# Print script name
print(f"Script name: {sys.argv[0]}")
