#!/usr/bin/python3
"""
handling HTTP errors
"""
from urllib import request, error
import sys 


if __name__ == "__main__":
XX= sys.argv[1]
    try:
        with request.urlopen(XX) as ry:
            by = ry.read()
            print(by.decode('utf-8'))
    except error.HTTPError as er:
        print(f"Error code: {er.code}")
