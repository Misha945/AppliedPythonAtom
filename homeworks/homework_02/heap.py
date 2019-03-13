#!/usr/bin/env python
# coding: utf-8


class Heap():

    def __init__(self, array):
        self.in_info = array[:]
        self.main = []
        self.build_heap()

    def add(self, prior_el):
        self.main.append(prior_el)
        i = len(self.main) - 1
        while i > 0:
            par = (i - 1)//2
            if comparator_d(self.main[i], self.main[par]):
                self.main[i], self.main[par] = self.main[par], self.main[i]
                i = par
            else:
                break

    def build_heap(self):
        i = 1
        if self.in_info:
            self.main.append(self.in_info[0])
            while i < len(self.in_info):
                self.add(self.in_info[i])
                i += 1


class MaxHeap(Heap):

    def __init__(self, array):
        Heap.__init__(self, array)
        raise NotImplementedError

    def extract_maximum(self):
        res = self.main[0]
        i = len(self.main) - 1
        self.main[0] = self.main[i]  # перемещаем последний элемент в корень
        self.main.pop()
        i = 0
        while 2*i+1 <= len(self.main) - 1:  # фактически метод shift down
            if 2*i+1 == len(self.main) - 1:  # случай единственного сына
                change_i = 2*i+1
                if comparator_d(self.main[change_i], self.main[i]):
                    temp = self.main[i]
                    self.main[i] = self.main[change_i]
                    self.main[change_i] = temp
                break
            else:  # случай двух сыновей
                child_l = 2*i+1
                child_r = 2*i+2
                if comparator_d(self.main[child_l], self.main[child_r]):
                    change_i = child_l
                else:
                    change_i = child_r
                if comparator_d(self.main[change_i], self.main[i]):
                    temp = self.main[i]
                    self.main[i] = self.main[change_i]
                    self.main[change_i] = temp
                i = change_i
        return res


def comparator_d(x, y):
    if x[0] == y[0]:
        return x[1] >= y[1]
    elif x[0] > y[0]:
        return True
    else:
        return False
