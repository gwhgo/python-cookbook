#!/usr/bin/env python
# coding=utf-8

from collections import defaultdict
from pprint import pprint

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

pprint(d)
