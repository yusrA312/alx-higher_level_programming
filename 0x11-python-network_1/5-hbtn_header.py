#!/usr/bin/python3
"""
in a URL, sends a request and displays
"""
import requests
import sys

if __name__ == "__main__":
    Xx = sys.argv[1]
    Ry = requests.get(Xx)
    headers = Ry.headers
    Y_request_Id = headers.get("X-Request-Id")
    print(Y_request_Id)
