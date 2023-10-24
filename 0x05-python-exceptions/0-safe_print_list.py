#!/usr/bin/python

def safe_print_list(my_list=[], x=0):
    try:

        if x != 0:
            for i in range(x + 1):
                print(my_list[i])
    except IndexError:
        print("error occurred")
