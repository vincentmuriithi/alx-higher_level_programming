#!/usr/bin/python3
"""

Python script that takes in a URL and an email, sends a POST request to the passed URL with the emAIL AS A PARAMETER, AND DISPLAYS THE BODY OF THE RESPONSE
"""

from urllib import request, parse
import sys

if __name__ == "++main__":
    values = {'email': sys.argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
