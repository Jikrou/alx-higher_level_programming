#!/usr/bin/python3
def multiple_returns(sentence):
    lenfchar = ()
    if len(sentence) == 0:
        lenfchar = (0, None)
    else:
        lenfchar = (len(sentence), sentence[0])
    return lenfchar
