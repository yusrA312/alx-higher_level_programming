#!/usr/bin/python3
"""
in a URL, sends a request and displays

"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as reyy:
        H = reyy.info()
        Yyget = H.get("X-Request-Id")
        print(Yyget)
