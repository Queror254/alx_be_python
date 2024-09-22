def calculator():
    # Get user input for numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Get user input for the operation
    operation = input("Choose the operation (+, -, *, /): ")

    # Perform the calculation using match-case
    match operation:
        case "+":
            result = num1 + num2
            print(f"The result is {result}")
        case "-":
            result = num1 - num2
            print(f"The result is {result}")
        case "*":
            result = num1 * num2
            print(f"The result is {result}")
        case "/":
            if num2 == 0:
                print("Cannot be divided by zero")
            else:
                result = num1 / num2
                print(f"The result is {result}")
        case _:
            print("Invalid operation selected. Please choose one of +, -, *, /.")

# Run the calculator
if __name__ == "__main__":
    calculator()

