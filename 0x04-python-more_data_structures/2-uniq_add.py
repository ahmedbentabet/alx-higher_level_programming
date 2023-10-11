#!/usr/bin/python3
def uniq_add(my_list=[]):

    track_set = set()
    for i in my_list:
        track_set.add(i)

    return sum(track_set)
