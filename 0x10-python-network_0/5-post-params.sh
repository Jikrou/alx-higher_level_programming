#!/bin/bash
# a bash script that take in a URL, send a post request to the passed url.
curl -sX POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
