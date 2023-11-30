#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    total = 0
    for user_input in argv[1:]:
        total += int(user_input)
    print("{:d}".format(total))
