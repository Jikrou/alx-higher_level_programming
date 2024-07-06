#!/usr/bin/python3
"""
a python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
    """
import requests
import sys


if __name__ == '__main__':

    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

    try:
        r_json = r.json()
        if r_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(r_json.get('id'), r_json.get('name')))
    except ValueError:
        print("Not a valid JSON")
