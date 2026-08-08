class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b


calculator = Calculator()

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("\nChoose operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        result = calculator.add(a, b)

    elif choice == "2":
        result = calculator.subtract(a, b)

    elif choice == "3":
        result = calculator.multiply(a, b)

    elif choice == "4":
        result = calculator.divide(a, b)

    else:
        raise ValueError("Invalid operation choice.")

    print("Result:", result)

except ValueError as e:
    print("Error:", e)

except ZeroDivisionError as e:
    print("Error:", e)
