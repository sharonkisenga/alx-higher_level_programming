#!/bin/bash
# script that takes in a URL, sends a POST
curl -sX POST $1 -d "email=test@gmail.com=I will always be here for PLD" -L
