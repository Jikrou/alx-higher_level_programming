#!/bin/bash
# Get the body size of the response
curl -sI "$1" | grep -i Content-Length | cut -d ' ' -f2
