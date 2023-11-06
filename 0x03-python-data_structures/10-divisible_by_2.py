#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    len_list = len(my_list)
    new_list = my_list.copy()
    if len_list == 0:
        return (None)
    for i in range(len_list):
        if my_list[i] % 2 == 0:
            new_list[i] = True
        else:
            new_list[i] = False
    return (new_list)
