#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    if number == 0:
        return 0
    number2 = number
    if number < 0:
        number = -number
    number = list(str(number))
    number.reverse()
    while number[0] == '0':
        number.pop(0)
    i = 0
    x = 0
    while i < len(number):
        x += int(number[i])*10**(len(number)-1-i)
        i += 1
    if number2 < 0:
        x *= -1
    return x
    raise NotImplementedError
