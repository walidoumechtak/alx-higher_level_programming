#!/usr/bin/python3
def multiple_returns(sentence):
    new_t = (len(sentence),)
    if new_t[0] == 0:
        new_t = new_t + (None,)
    else:
        new_t = new_t + (sentence[0],)
    return new_t
