#!/usr/bin/env python
# coding: utf-8


def revert_linked_list(head):
    back = None
    c = head
    while c:
        f = c.next_node
        c.next_node = back
        back = c
        c = f
    return back
    raise NotImplementedError
