#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator <a> <operator> <b>")
        quit(1)
    a = int(argv[1])
    b = int(argv[3])
    ops = ["+", "-", "*", "/"]
    from calculator_1 import add, sub, mul, div
    funcs = [add, sub, mul, div]
    for index, operator in enumerate(ops):
        if argv[2] == operator:
            print("{} {} {} = {}".format(a, operator, b, funcs[index](a, b)))
            break
    else:
        print("Unknown operator. Available operators are: +, -, * and /")
        quit(1)
