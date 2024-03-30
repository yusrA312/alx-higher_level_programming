#!/usr/bin/python3
"""A python that fetches """

if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resyy:
        content = resyy.read()
        print(f"Body response:\n\t- type: {type(content)}\n\t- content: {content}\n\t- utf8 content: {content.decode('utf-8')}")
