#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    from sys import argv
    argslen = len(argv) - 1;
    if (argslen == 1):
        print("1 argument:")
        print("1: {}".format(argv[1]))
    elif (argslen > 1):
        print("{} arguments:".format(argslen))
        for i in range(1,argslen +1):
            print("{}: {}".format(i, argv[i]))
    else:
        print("0 arguments.")
