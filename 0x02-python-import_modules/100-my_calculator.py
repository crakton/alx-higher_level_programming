#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, operator, b = sys.argv[1:]

    if operator not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a, b = int(a), int(b)

    if operator == "+":
        result = add(a, b)
    elif operator == "-":
        result = sub(a, b)
    elif operator == "*":
        result = mul(a, b)
    else:  # operator == "/"
        result = div(a, b)

    print("{} {} {} = {}".format(a, operator, b, result))
