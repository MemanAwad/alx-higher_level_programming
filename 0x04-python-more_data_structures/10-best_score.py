#!/usr/bin/python3
def best_score(a_dictionary):
    if not len(a_dictionary) == 0:
        return (None)

    maxx = list(a_dictionary.keys())[0]
    bkey = a_dictionary[maxx]
    for x, y in a_dictionary.items():
        if y < bkey:
            bkey = y
            maxx = x
    return (maxx)
