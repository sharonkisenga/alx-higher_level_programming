#!/bin/bash
# script that takes in a URL
curl -sI ALLOW $1 -L | grep "Allow" | cut -d " " -f2-
