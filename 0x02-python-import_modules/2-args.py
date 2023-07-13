#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    strong = len(argv) - 1
    if strong == 0:
        print("{}".format("0 arguments."))
    elif strong == 1:
        print("{}".format("1 argument:"))
        print("{}".format(argv[1]))
    else:
        print("{:d} {}".format(strong, "arguments:"))
        for i in range(1, strong + 1):
            print("{:d}: {}".format(i, argv[i]))



