#!/usr/bin/env python3

# Author: Edwin Roshy
# Author ID: 169475233
# Date Created: 2025/05/21

import sys

# Set default value or use command-line argument
if len(sys.argv) == 2:
    timer = int(sys.argv[1])
else:
    timer = 3

# Countdown loop
while timer != 0:
    print(timer)
    timer = timer - 1

print('blast off!')
