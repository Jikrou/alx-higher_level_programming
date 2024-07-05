#!/usr/bin/python3
"""
    a script that takes in a url, sends a request to the url and displays
    the value of the X-Request-Id variable found in the header
"""

if __name__ == '__main__':
    import requests
    import sys

    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
