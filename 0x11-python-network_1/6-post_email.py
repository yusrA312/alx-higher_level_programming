#!/usr/bin/python3
"""
request to the passed URL with the email as a parameter"""


if __name__ == '__main__':
    from sys import argv
    from requests import post

    Uy = argv[1]
    Ey = argv[2]
    Ry = post(Uy, {'email': Ey})
    print(Ry.text)
