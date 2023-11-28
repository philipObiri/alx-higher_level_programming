#!/usr/bin/python3
def remove_char_at(str, index):
    if index >= 0:
        newstr = str[:index] + str[index + 1:]
        return (newstr)
    else:
        return (str)
