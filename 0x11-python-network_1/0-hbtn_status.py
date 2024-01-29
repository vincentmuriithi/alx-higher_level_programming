#!/usr/bin/env python3
#This script fethes a url usind urllib

import urllib.request as r

req = r.Request("https://alx-intranet.hbtn.io/status")
with r.urlopen(req) as response:
    response.read()
