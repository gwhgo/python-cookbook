#!/usr/bin/env python
# coding=utf-8

# If the values in the sequence are hashable, the problem can be easily sovled using a set and a generator.
#def dedupe(items):
#    seen = set()
#    for item in items:
#        if item not in seen:
#            yield item
#            seen.add(item)
#
#if __name__ == "__main__":
#    a = [1, 5, 2, 1, 9, 1, 5, 10]
#    print(list(dedupe(a)))

#This only works if the items in the sequence are hashable. 
#If you are trying to eliminate duplicates in a sequence of unhashable types (such as dicts), you can make a slight change to this recipe

def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

if __name__ == "__main__":
    a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4} ]
    print(list(dedupe(a,lambda d:(d['x'],d['y']))))

