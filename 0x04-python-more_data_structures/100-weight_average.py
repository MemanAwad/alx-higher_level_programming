#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return 0
    summ, avg = 0, 0
    for x in my_list:
        summ += x[0] * x[1]
        avg += x[1]
    return (summ / avg)
