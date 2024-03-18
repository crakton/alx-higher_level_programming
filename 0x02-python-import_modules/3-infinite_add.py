#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    sum = 0
    argslen = len(argv)

    if (argslen == 1):
        print(sum)
    else:
        for i in range(1, argslen):
            sum += int(argv[i])
        print("{}".format(sum))
