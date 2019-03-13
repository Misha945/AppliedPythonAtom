#!/usr/bin/env python
# coding: utf-8


def listminus(ks, vs, KS, VS):
    k = 0
    if (type(vs) == list or type(vs) == set or
        type(vs) == tuple):
        k += 1
        if type(vs) == set:
            vs = list(vs)
        for i in range(len(vs)):
            listminus(ks, vs[i], KS, VS)
    else:
        VS.append(ks)
        KS.append(vs)
        

def invert_dict(source_dict):
    keys = list(source_dict.keys())
    values = list(source_dict.values())
    keys2 = []
    values2 = []

    for i in range(len(values)):
        listminus(keys[i],values[i],keys2,values2)

    i = 0
    l = [l * 0 for l in range(len(keys2))]

    repeat = 1
    while i < len(keys2):
        k = i + 1
        while k < len(keys2):
            if keys2[k] == keys2[i] and l[k] == 0:
                l[i] = repeat
                l[k] = repeat
            k += 1
        repeat += 1
        i += 1
    keys3 = []
    values3 = []
    for i in range(len(keys2)):
        if l[i] == 0:
            keys3.append(keys2[i])
            values3.append(values2[i])
    i = 1
    while i <= max(l):
        k = 0
        repeat = 0
        help_list = []
        while k < len(values2):
            if l[k] == i:
                help_list.append(values2[k])
                if repeat == 0:
                    keys3.append(keys2[k])
                    repeat += 1
            k += 1
        if len(help_list) != 0:
            values3.append(help_list)
        i += 1
    new_dict = {}
    for a in range(len(values3)):
        new_dict[keys3[a]] = values3[a]
    return new_dict
    raise NotImplementedError
