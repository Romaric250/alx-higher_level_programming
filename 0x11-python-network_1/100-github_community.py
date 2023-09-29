#!/usr/bin/python3
""" this script list the 10 most recent commits in a repo"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    req = requests.get(url)
    com = req.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                com[i].get("sha"),
                com[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
