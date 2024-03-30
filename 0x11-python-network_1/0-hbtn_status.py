#!/usr/bin/python3
"""A Python script that fetches content from a URL."""

if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as ryy:
        html = ryy.read()
        print("Body response:")
        print(f"\t- type: {type(html)}\n\t- content: {html}\n\t- " +
              f"utf8 content: {html.decode('utf-8')}")
