#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    from sys import argv
    argslen = len(argv)
    if (argslen > 1):
        print("{} arguments:".format(argslen))
        for i in range(1,argslen):
            print("{}: {}".format(i, argv[i]))
    else:
        print("0 arguments.")
