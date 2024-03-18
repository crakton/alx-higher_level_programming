#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    sum = 0
    argslen = len(argv)

    if (argslen == 2 and len(argv[1]) > 1000):
        args = argv[1].split();
    else:
        args = argv[1:]

    for arg in args:
        sum += int(arg)
    print("{}".format(sum))
