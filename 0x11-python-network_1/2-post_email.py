#!/usr/bin/python3
""" this scripts Sends a POST request to a given URL with a given email.
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    mail = {"email": sys.argv[2]}
    data_mail = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data_mail)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
