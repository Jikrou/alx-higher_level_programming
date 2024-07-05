#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/ and display the value of
the X-Request-Id variable found in the header of the response
"""

if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as res:
        print(res.info().get("X-Request-Id"))
