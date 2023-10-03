#!/usr/bin/python3
for i in range(0, 100):
    if i == 99:
        print("{}".format(i))
    elif i < 99:
        print("{0:02d}".format(i), end=', ')
