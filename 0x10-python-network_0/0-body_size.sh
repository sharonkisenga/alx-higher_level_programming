#!/bin/bash
# script that takes in a URL
curl -Is "$1" | grep -w 'Content-Length' | cut -f2 -d' '
