#!/usr/bin/env python
# coding: utf-8


def calculate_determinant(list_of_lists):
    k = 0
    while k < len(list_of_lists):
        if len(list_of_lists[k]) != len(list_of_lists):
            return None
        k += 1
    if len(list_of_lists) == 1:
        return list_of_lists[0][0]
    if len(list_of_lists) == 2:
        a11 = list_of_lists[0][0]
        a22 = list_of_lists[1][1]
        a12 = list_of_lists[0][1]
        a21 = list_of_lists[1][0]
        return a11*a22-a12*a21
    k = 0
    result = 0
    while k < len(list_of_lists):
        i = 0
        help_list = list_of_lists.copy()
        while i < len(list_of_lists):
            help_list[i] = list_of_lists[i].copy()
            i += 1
        help_list.pop(0)
        i = 0
        while i < len(list_of_lists) - 1:
            help_list[i].pop(k)
            i += 1
        result += (-1)**k*list_of_lists[0][k]*calculate_determinant(help_list)
        k += 1
    return result
    raise NotImplementedError