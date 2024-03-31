#!/usr/bin/python3
"""Python script that sends a request to the URL and
   displays the value of a variable in the response header   """
   import sys
   import requests


   if __name__ == "__main__":
       url = "https://api.github.com/repos/{}/{}/commits".format(
		               sys.argv[2], sys.argv[1])

           r = requests.get(url)
