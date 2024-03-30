#!/usr/bin/python3
"""A python that fetches """

if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as reyy:
        content = reyy.read()
      print(f"Body response:\n"
          f"\t- type: {type(content)}\n"
          f"\t- content: {content}\n"
          f"\t- utf8 content: {content.decode('utf-8')}")
