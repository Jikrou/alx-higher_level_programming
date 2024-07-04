#!/bin/bash
# Script to GET a URL, follow redirects, and display the body of a 200 status response
curl -sL "$1"
