#!/usr/bin/python3
"""
A script that:
    - takes in a URL,
    - sends a request to the URL and displays the value
    - of the X-Request-Id variable found inthe header of the response
"""

import sys, urllib.request as re


if __name__ == "__main__":
    url = sys.argv[1]

    request = re.Request(url)
    with re.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
