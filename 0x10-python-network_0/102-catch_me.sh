#!/bin/bash
# Displays the size of the body of the response
curl -sL 0.0.0.0:5000/catch_me -X PUT -d "user_id=98" -H 'Origin: HolbertonSchool'