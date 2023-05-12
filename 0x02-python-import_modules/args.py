#!/usr/bin/python3
import sys
if __name__ == "__main__":
    length = len(sys.argv)
    if length <= 1:
        print("0 arguments.")
    else:
        print("{:d}: argument:".format(length - 1))
        for i in range(1, length):
            print("{:d}: {}".format(i, sys.argv[i]))
