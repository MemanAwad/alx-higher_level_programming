#!/usr/bin/python3
for alpha in range(122, 96, -1):
    if alpha % 2 == 0:
        ch = chr(alpha)
    else:
        ch = chr(alpha - 32)
    print("{}".format(ch), end="")
