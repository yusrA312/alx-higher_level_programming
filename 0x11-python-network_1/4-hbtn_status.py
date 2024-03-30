#!/usr/bin/python3
"""A Python script that fetches content from a URL."""
import requests

if __name__ == '__main__':
    U = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(U)
    
    HT = response.content
    print("Body response:")
    print(f"\t- type: {type(HT)}\n\t- content: {html}")
