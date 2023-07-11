#!/usr/bin/python3
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - 1)), end="")
    c = 32 if c == 0 else 0
