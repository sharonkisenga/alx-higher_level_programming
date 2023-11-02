#!/bin/bash
# Write a Bash script that sends a JSON
curl -sX POST $1 -H "Content-Type: application/json" -d @$2 -L
