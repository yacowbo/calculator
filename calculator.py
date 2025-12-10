#!/usr/bin/env python3

# this is the calculator module
def calculate(a, b, op):
    a = input("Please enter your input for input a: ")
    while (a != float or int):
        try:
            (a == float or int)
        except ValueError:
            return "Error: Please enter valid numbers for input a."

        b = input("Please enter your input for input b: ")
        try:
            (b == float or int)
        except ValueError:
            return "Error: Please enter valid numbers for input b."

    match op:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            if b == 0:
                return "Error: Cannot divide by zero."
            return a / b
        case _:
            return "Error: Unsupported operation."

# simple driver program to test the calculator
def main():
    print("CLI Calculator")
    print("Enter your operation (e.g. 3.5 * 4):")
    try:
        expr = input("> ").split()
        if len(expr) != 3:
            raise ValueError
        a, op, b = expr
        result = calculate(a, b, op)
        print("Result:", result)
    except ValueError:
        print("Error: Please enter in format 'number operator number'.")

# i dont even know what this does
if __name__ == "__main__":
    main()
