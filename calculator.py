#!/usr/bin/env python3

def calculate(a, b, op):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return "Error: Please enter valid numbers."

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

if __name__ == "__main__":
    main()
