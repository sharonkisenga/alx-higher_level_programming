#!/bin/bash
# script that makes a request
curl -sLX PUT '' -H "Origin: School" 0.0.0.0:5000/catch_me -d "user_id=98"
