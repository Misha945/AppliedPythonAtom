#!/usr/bin/env python
# coding: utf-8


def groupping_anagramms(words):
    dict1 = {}
    for i in words:
        x = ''.join(sorted(i.lower()))
        if x in dict1.keys():
            dict1[x].append(i)
        else:
            dict1[x] = [i]
    return list(dict1.values())
    raise NotImplementedError
