#!/usr/bin/python3
def text_indentation(text):
    contr = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(0, len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i], end='')
            print("")
            print("")
            if text[i + 1] == ' ':
                contr = 1

            else:
                contr = 0
        else:
            if contr == 0:
                print(text[i], end='')
            contr = 0
