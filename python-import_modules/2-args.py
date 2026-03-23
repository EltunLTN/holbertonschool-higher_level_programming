#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
        print("1: {argv[1]}".format(argv=argv))
    else:
        print("{argc} arguments:".format(argc=argc))
        for i in range(1, argc + 1):
            print("{i}: {argv[i]}".format(i=i, argv=argv))
