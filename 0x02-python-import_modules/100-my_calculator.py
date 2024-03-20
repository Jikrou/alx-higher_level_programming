#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])
    operators = ["+", "-", "/", "*", "⁎"]

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if operator in operators:
        if operator == "-":
            result = sub(a, b)
        elif operator == "/":
            result = div(a, b)
        elif operator == "+":
            result = add(a, b)
        elif operator == "⁎" or operator == "*":
            result = mul(a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
