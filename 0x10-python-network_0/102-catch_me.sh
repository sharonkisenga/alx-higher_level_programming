#!/bin/bash
# script that makes a request
curl -o /dev/null -sw "You got me!" 0.0.0.0:5000/catch_me
