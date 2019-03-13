#!/usr/bin/env python
# coding: utf-8


from homeworks.homework_02.heap import MaxHeap
from homeworks.homework_02.fastmerger import FastSortedListMerger


class VKPoster:

    def __init__(self):
        self.users = {}
        self.posts = {}
        raise NotImplementedError
        
    def create_user(self, user_id):
        self.users.update({user_id: []})

    def user_posted_post(self, user_id: int, post_id: int):
        if self.users.get(user_id) is None:
            self.create_user(user_id)
        self.posts.update({post_id: []})

    def user_read_post(self, user_id: int, post_id: int):
        if self.posts.get(post_id) is None:
            self.posts.update({post_id: ['somebody']})
        self.posts[post_id].append(user_id)

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        if self.users.get(follower_user_id) is None:
            self.create_user(follower_user_id)
        if self.users.get(follower_user_id) is None:
            self.create_user(followee_user_id)
        self.users[follower_user_id].append(followee_user_id)

    def get_recent_posts(self, user_id: int, k: int)-> list:
        help_list = []
        res = []
        for i in self.posts.keys():
            try:
                self.users[user_id].index(self.posts[i][0])
            except ValueError:
                pass
            else:
                try:
                    self.posts[i].index(user_id)
                except ValueError:
                    help_list.append((len(self.posts[i])-1, i))
        h = MaxHeap(help_list)
        i = 0
        while i < k:
            res.append(h.extract_maximum()[1])
            i += 1
        return res

    def get_most_popular_posts(self, k: int) -> list:
        help_list = []
        res = []
        for i in self.posts.keys():
            help_list.append((len(self.posts[i])-1, i))
        h = MaxHeap(help_list)
        while i < k:
            res.append(h.extract_maximum()[1])
            i += 1
        return res
