#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("{}".format(0))
    if len(sys.argv) == 2:
        print("{}".format(int(sys.argv[1])))
    if len(sys.argv) > 2:
        arg_sum = 0
        for i in range(len(sys.argv) - 1):
            arg_sum += int(sys.argv[i + 1])
        print("{}".format(arg_sum))
