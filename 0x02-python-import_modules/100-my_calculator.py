#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, operator, b = sys.argv[1:]

    if operator not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a, b = int(a), int(b)

    ops = {"+": calculator_1.add, "-": calculator_1.sub, "*": calculator_1.mul, "/": calculator_1.div}

    if operator == "*":
        result = calculator_1.mul(a, b)
    else:
        result = ops[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
