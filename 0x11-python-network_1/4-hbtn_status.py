#!/usr/bin/python3
"""This modules defines a task"""

import requests


if __name__ == "__main__":
    req = requests.get('https://intranet.hbtn.io/status')
    text = req.text
    print('Body response:')
    print('\t- type: {}'.format(type(text)))
    print('\t- content: {}'.format(text))
