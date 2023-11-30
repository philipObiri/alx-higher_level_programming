#!/usr/bin/python3
import sys

def print_command_line_arguments():
    number_of_command_line_arguments = len(sys.argv) - 1
    if number_of_command_line_arguments == 0:
        print("0 arguments.")
    elif number_of_command_line_arguments == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(number_of_command_line_arguments))
    for i in range(number_of_command_line_arguments):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))

if __name__ == "__main__":
    print_command_line_arguments()
