#!/usr/bin/python3
"""This modules defines a task"""

import requests
from sys import argv


if __name__ == "__main__":
    q = argv[1] if len(argv) > 1 else ""
    try:
        req = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
        req = req.json()
        if 'id' in req and 'name' in req:
            print("[{}] {}".format(req['id'], req['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
