from custom_modules.mathematical_operations import calculations

try:
    data = calculations(*input("Enter first number, operator, second number: ").split())
    print(f"Result is: {data:.2f}")
except ValueError:
    print("Enter a valid data!")
