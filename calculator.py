def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


def show_menu():
    print("\n==== CLI CALCULATOR ====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")


def main():
    while True:
        show_menu()
        
        choice = input("Enter your choice (1-5): ")

        # Exit condition
        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        # Validate choice
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        if choice == '1':
            result = add(num1, num2)
            print(f"Result: {result}")

        elif choice == '2':
            result = subtract(num1, num2)
            print(f"Result: {result}")

        elif choice == '3':
            result = multiply(num1, num2)
            print(f"Result: {result}")

        elif choice == '4':
            result = divide(num1, num2)
            print(f"Result: {result}")


if __name__ == "__main__":
    main()