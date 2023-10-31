#!/usr/bin/python
def remove_char_at(str, n):
    str2 = ""
    for i in range(len(str)):
        if (i == n):
            continue
        else:
            str2 = str2 + str[i]
    return (str2)
