#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response."""

from requests import post


def suser(Q):
    """Sends a req."""
    U = 'http://0.0.0.0:5000/search_user'
    data = {'q': Q}
    response = post(U, data)

    tyes = response.headers['content-type']

    if tyes == 'application/json':
        result = response.json()
       U_id = result.get('id')
        name = result.get('name')
        if result and U_id and name:
            return "[{}] {}".format(U_id, name)
        else:
            return 'No result'
    else:
        return 'Not a valid JSON'


if __name__ == '__main__':
    from sys import argv

    Q = argv[1] if len(argv) >= 2 else ""
    print(suser(Q))
