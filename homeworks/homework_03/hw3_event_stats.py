#!/usr/bin/env python
# coding: utf-8


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        self.dict = {}
        raise NotImplementedError

    def register_event(self, user_id, time):
        if user_id in self.dict.keys():
            self.dict[user_id].append(time)
        else:
            self.dict[user_id] = [time]
        raise NotImplementedError

    def query(self, count, time):
        res = []
        for i, k in self.dict.items():
            s = sum(time - 300 < x < time for x in k)
            if s == 0 and count == 0:
                continue
            if s == count:
                res.append(i)
        return len(res)
        raise NotImplementedError
