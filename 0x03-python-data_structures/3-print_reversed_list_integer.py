#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new_list = my_list.copy()
    new_list.sort(reverse=True)
    for i in new_list:
        print("{:d}".format(i))
