#!/usr/bin/python3
"""
a python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
    """

if __name__ == '__main__':
    import requests
    import sys

    if len(sys.argv[1]) > 1:
        q = sys.argv[1]
    else:
        q = ""

    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        r = r.json()
        if r == {}:
            print("No result")
        else:
            print("[{}] {}".format(r.get('id'), r.get('name')))
    except ValueError:
        print("Not a valid JSON")
