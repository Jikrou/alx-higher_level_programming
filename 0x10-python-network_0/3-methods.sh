#!/bin/bash
# a bash script that takes in a URL and displays all th HTTP methods the server will accept.
curl -sI "$1" | grep -i allow | cut -d ":" -f2 | tr -d " "
