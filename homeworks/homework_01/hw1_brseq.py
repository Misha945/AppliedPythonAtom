#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    stack = []
    i = 0
    while i < len(input_string):
        if (input_string[i] == '(' or
           input_string[i] == '[' or
           input_string[i] == '{'):
            stack.append(input_string[i])
        else:
            if not stack:
                return False
            if not((input_string[i] == ')' and stack.pop() == '(')
               or (input_string[i] == ']' and stack.pop() == '[')
               or (input_string[i] == '}' and stack.pop() == '{')):
                return False
        i += 1
    if stack:
        return False
    else:
        return True
    raise NotImplementedError
