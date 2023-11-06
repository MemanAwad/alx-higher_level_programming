#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    # first tuple
    if len1 == 0:
        x, y = 0, 0
    elif len1 == 1:
        x = tuple_a[0]
        y = 0
    else:
        x = tuple_a[0]
        y = tuple_a[1]
    # second tuple
    if len2 == 0:
        w, z = 0, 0
    elif len2 == 1:
        w = tuple_b[0]
        z = 0
    else:
        w = tuple_b[0]
        z = tuple_b[1]
    # result tuple
    tuple_c = (x+w, z+y)
    return (tuple_c)
