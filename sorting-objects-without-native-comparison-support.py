#!/usr/bin/env python
# coding=utf-8

from operator import attrgetter
class User:
    def __init__(self,user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)

u1 = User(1)
u2 = User(2)

print(sorted([u2,u1],key = lambda u: u.user_id))

print(sorted([u2,u1],key=attrgetter('user_id')))
#print(attrgetter('user_id'))
