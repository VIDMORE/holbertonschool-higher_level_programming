#!/bin/bash
# Displays the size of the body of the response
curl -sw '%{http_code}' $1 -o /dev/null
