#!/usr/bin/python3
def multiple_returns(sentence):
    len_sentence = len(sentence)
    firstc = ""
    if len_sentence == 0:
        firstc = None
    else:
        firstc = sentence[0]
    tupule = (len_sentence, firstc)
    return (tupule)
