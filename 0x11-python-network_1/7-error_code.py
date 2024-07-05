#!/usr/bin/python3
"""
    Script that takes in a URL, sends a requests to the URL
    and displays the body of the response.
    if the HTTP status code is greater than or equal to 400
    print Error code: followed by the value of the HTTP status code
"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    r = requests.get(url)

    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
