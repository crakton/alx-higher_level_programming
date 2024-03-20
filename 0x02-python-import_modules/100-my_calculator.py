#!/usr/bin/python3

if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operations = {"+": add, "-": sub, "*": mul, "/": div}
    a, op, b = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])

    if op not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{} {} {} = {}".format(a, op, b, operations[op](a, b)))
