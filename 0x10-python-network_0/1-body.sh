#!/bin/bash
# takes in a URL, sends GET request to URL, and displays the body of response
curl - sfL "$1" - X GET

