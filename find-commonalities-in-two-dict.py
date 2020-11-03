#!/usr/bin/env python
# coding=utf-8

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

print("--------a---------")
print(a)
print("--------b---------")
print(b)

# Find keys in common
print("Find keys in common")
_ = a.keys() & b.keys()
print(_)

# Find keys in a that are not in b
print("Find keys in a that are not in b")
_ = a.keys() - b.keys()
print(_)


# Find (key,value) pairs in common
print("Find (key,value) pairs in common")
_ = a.items() & b.items()
print(_)


# Make a new dictionary with certain keys removed 
print("Make a new dicionary with certain keys removed")
_ = { key:a[key] for key in a.keys() - {'z','w'} }
print(_)
