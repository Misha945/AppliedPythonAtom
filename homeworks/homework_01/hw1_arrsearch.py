#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    if len(input_list) == 0:
        return None
    if input_list is None:
        return None
    dict1 = {}
    for i in range(len(input_list)):
        dict1[input_list[i]] = i
    for i in dict1.keys():
        if dict1.get(n-i) is not None and dict1.get(n-i) != dict1[i]:
            return (dict1[i], dict1.get(n-i))
    return None
    raise NotImplementedError
