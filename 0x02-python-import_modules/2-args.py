#!/usr/bin/python3
from sys import argv

argslen = len(argv)
if (argslen > 1):
    print("{} arguments:".format(argslen))
    for i in range(1,argslen):
        print("{}: {}".format(i, argv[i]))
else:
    print("0 arguments.")
