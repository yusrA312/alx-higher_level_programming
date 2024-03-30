#!/usr/bin/python3
""" Handles HTTP errors.
"""
import sys
import requests


if __name__ == "__main__":
    U = sys.argv[1]

    rQ = requests.get(U)
    if rQ.status_code >= 400:
        print(f"Error code: {rQ.status_code}")
    else:
        print(rQ.text)
