#!/usr/bin/python3
for xup in range(ord('a'), ord('z') + 1):
    if chr(xup) != 'q' and chr(xup) != 'e':
        print("{}".format(chr(xup)), end='')
