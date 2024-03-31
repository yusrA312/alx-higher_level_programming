#!/usr/bin/python3
"""script that sends a request to the URL
"""
from sys import argv
import requests


if __name__ == "__main__":
    U = "https://api.github.com/repos/{}/{}/commits".format(
        argv[2], argv[1])

    hhh = requests.get(U)
