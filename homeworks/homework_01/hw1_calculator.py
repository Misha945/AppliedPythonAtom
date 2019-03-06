#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    if type(x) != int and type(x) != float:
        return None
    if type(y) != int and type(y) != float:
        return None
    if operator == 'plus':
        return x+y
    if operator == 'minus':
        return x-y
    if operator == 'mult':
        return x*y
    if operator == 'devide' and y != 0:
        return x/y
    return None
    raise NotImplementedError
