#!/usr/bin/python3
for character in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format((character - (ord('a') - ord('A'))) if character % 2 else c), end='')
