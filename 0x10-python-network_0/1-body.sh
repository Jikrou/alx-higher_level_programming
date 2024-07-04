#!/bin/bash
#a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response.
curl -sL -w '\n%{http_code}' "$1" | sed -n '1,/^200$/!d;/^200$/q;p'
