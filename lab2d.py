#!/usr/bin/env python3

import sys

# Check if exactly 2 additional arguments are provided (total length should be 3)
if len(sys.argv) != 3:
    print('Usage: ' + sys.argv[0] + ' name age')
    sys.exit()

name = sys.argv[1]
age = sys.argv[2]

print('Hi ' + name + ', you are ' + age + ' years old.')
