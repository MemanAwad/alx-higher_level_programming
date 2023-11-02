#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    if (length == 1):
        print("0")
    else:
        summ = 0
        for i in range(1, length):
            summ += (int)(sys.argv[i])
        print("{}" .format(summ))
