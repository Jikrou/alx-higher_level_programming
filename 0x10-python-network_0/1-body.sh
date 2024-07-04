#!/bin/bash
#a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response.
curl -sI "$1" | grep -i Location | cut -d ' ' -f2 | cut -d '/' -f2 | sed 's/_/ /g'
