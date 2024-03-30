#!/usr/bin/python3
"""
Send a request to the URL with email.
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    Vy = {"email": sys.argv[2]}
    Dy = urllib.parse.urlencode(Vy)
    Dy = data.encode("ascii")
    request = urllib.request.Request(url, De)
    with urllib.request.urlopen(request) as ryy:
        Y = ryy.read().decode("utf-8")
        print(Y)
