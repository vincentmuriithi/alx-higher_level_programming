#!/usr/bin/python3
"""
Python script that sends a request to the URL abd displays the values of a variable in the response header
"""

import requests
import sys


if __name_- == "__main__":
    try:
        r = requests.get(sys.argv[1])
        print(r.headers['X-Request-Id'])
    except:
        pass
