#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response."""

from requests import post


def search_user(query):
    """Sends a request to the URL and displays the body of the response."""
    URL = 'http://0.0.0.0:5000/search_user'
    data = {'q': query}
    response = post(URL, data)

    type_res = response.headers['content-type']

    if type_res == 'application/json':
        result = response.json()
        _id = result.get('id')
        name = result.get('name')
        if result and _id and name:
            return "[{}] {}".format(_id, name)
        else:
            return 'No result'
    else:
        return 'Not a valid JSON'


if __name__ == '__main__':
    from sys import argv

    query = argv[1] if len(argv) >= 2 else ""
    print(search_user(query))
