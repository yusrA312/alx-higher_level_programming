#!/usr/bin/python3
"""script that takes your GitHub"""
import requests
from sys import argv


def getid(Uname, Pword):
    U = f"https://api.github.com/user"
    headers = {"Authorization": f"token {Pword}"}
    response = requests.get(U, headers=headers)
    if response.status_code == 200:
        udata = response.json()
        if "id" in udata:
            return udata["id"]
    return None


if __name__ == "__main__":
    Uname = argv[1]
    Pword = argv[2]

    u_id = getid(Uname, Pword)
    print(u_id)
