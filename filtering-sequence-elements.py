#!/usr/bin/env python
# coding=utf-8

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# Use list or generator comprehension
print([ x for x in mylist if x > 0 ])

pos = ( x for x in mylist if x > 0 )
for x in pos:
    print(x)

# Use built-in filter funciton
values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int,values))

print(ivals)



