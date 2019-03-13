#!/usr/bin/env python
# coding: utf-8

from .heap import MaxHeap


class FastSortedListMerger:

    @staticmethod
    def merge_first_k(list_of_lists, k):
        res = []
        help_list = []
        i = 0
        while i < len(list_of_lists):  # o(N)
            if list_of_lists[i]:
                help_list.append((list_of_lists[i][-1], i))
            i += 1
        l = MaxHeap(help_list)  # o(N)
        i = 0
        while i < k:  # o(k)
            maxx = l.extract_maximum()  # o(log(N))
            res.append(maxx[0])
            list_of_lists[maxx[1]].pop()
            if list_of_lists[maxx[1]]:
                l.add((list_of_lists[maxx[1]][-1], maxx[1]))  # o(log(N))
            i += 1
        return res
        raise NotImplementedError
