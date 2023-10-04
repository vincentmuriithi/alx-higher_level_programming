#!/usr/bin/python3

def islower(c):
    # Check if the Unicode code point of c is within the range of lowercase letters
    return ord('a') <= ord(c) <= ord('z')
