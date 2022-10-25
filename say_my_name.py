#!/usr/bin/python

# Example Python script

import sys
argc = len(sys.argv)

if argc > 1:
    print('Too many Args')
    print("How did that happen")
else:
    where = 'World'
    print("Hello", where)

print('Goodbye from ' + sys.argv[0])