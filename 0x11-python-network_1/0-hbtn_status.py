#!/usr/bin/python3
"""Fetch from given URL using `urllib` package"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as res:
        content = res.read()
        print("Body response:")
        print("    - type: {}".format(type(content)))
        print("    - content: {}".format(content))
        print("    - utf8 content: {}".format(content.decode('utf-8')))
