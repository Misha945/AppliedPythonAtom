#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    if len(input_list) == 0:
        return None
    if input_list is None:
        return None
    res = []
    i = 0
    k = len(input_list) - 1
    input_list.sort()
    while (i != k):
        sum = input_list[i] + input_list[k]
        if (sum > n):
            k -= 1
        elif (sum < n):
            i += 1
        else:
            res.append(i)
            res.append(k)
            return tuple(res)
    return None
    raise NotImplementedError
