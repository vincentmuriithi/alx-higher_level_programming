#!/usr/binpython3
"""
A script that:
    -takes in a URL,
    - sends a request to the URL and displays the value
"""
import sys
import urllib.request as r

if __name__ == "__main__":
    url = sys.argv[1]
    request = r.Request(url)
    with r.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
