#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0 and n <= len(str):
        for i in range(len(str)):
            result = ""
            if i != n:
                result += s[i]
        return (result)
    else:
        return s
