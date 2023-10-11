#!/usr/bin/python3
def lookup(obj):
    return [attr for attr in dir(obj) if not callable(getattr(obj,attr))]
