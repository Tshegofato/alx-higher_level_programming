#!/bin/bash
# This script sends a GET request to the provided URL
# and displays the size of the response body in bytes.

curl - sI "$1" |
grep - i "content-length" |
awk '{print $2}'
