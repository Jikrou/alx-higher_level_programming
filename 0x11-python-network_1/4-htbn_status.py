#!/usr/bin/python3
"""
    a python script that fetches https://intranet.hbtn.io/status
"""

if __name__ == '__main__':
    import requests

    r = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- tyoe: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
