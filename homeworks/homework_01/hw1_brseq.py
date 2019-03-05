#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    a = 0
    b = 0
    c = 0
    i = 0
    while i < len(input_string):
        if input_string[i] == '(':
            a += 1
        if input_string[i] == '[':
            b += 1
        if input_string[i] == '{':
            c += 1
        if input_string[i] == ')':
            a -= 1
        if input_string[i] == ']':
            b -= 1
        if input_string[i] == '}':
            c -= 1
        if (a < 0) or (b < 0) or (c < 0):
            return False
        i += 1
    if (a**2 + b**2 + c**2) == 0:
        return True
    else:
        return False
    raise NotImplementedError
