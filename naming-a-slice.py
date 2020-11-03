#!/usr/bin/env python
# coding=utf-8
record = '....................100          .......513.25     ..........'

SHARES = slice(20,32)
PRICE = slice(40,48)

cost = int(record[SHARES]) * float(record[PRICE])

print(cost)
